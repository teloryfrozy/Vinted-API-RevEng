"""
TODO:
- add a input front to select the number of n last ads to refresh
- finish the refresh ads function
"""

import requests
import re
from time import sleep
from typing import List
from fastapi import APIRouter, Depends
from pydantic import BaseModel
from utils import execute_request, get_vinted_headers
from constants import API_URL
from sqlmodel import Session, select
from config.models import User, get_session

router = APIRouter(
    prefix="/ads-management",
)


class PhotoThumbnail(BaseModel):
    type: str
    url: str


class Photo(BaseModel):
    thumbnails: List[PhotoThumbnail]


class Price(BaseModel):
    currency_code: str
    amount: float


def extract_photos_urls(photos: List[Photo]) -> List[str]:
    """Extracts photo URLs from photos data"""
    urls = []
    for photo in photos:
        for thumbnail in photo.thumbnails:
            if thumbnail.type == "thumb364x428":
                urls.append(thumbnail.url)
    return urls


def prepare_item_info(item_data: dict) -> dict:
    """Prepares item info for re-upload"""
    color_ids = [
        color_id
        for color_id in [item_data["color1_id"], item_data["color2_id"]]
        if color_id is not None
    ]

    return {
        "id": None,
        "currency": item_data["price"]["currency_code"],
        "title": item_data["title"],
        "description": item_data["description"],
        "brand_id": item_data["brand_id"],
        "brand": item_data["brand"],
        "size_id": item_data["size_id"],
        "catalog_id": item_data["catalog_id"],
        "isbn": item_data["isbn"],
        "is_unisex": item_data["is_unisex"],
        "is_for_sell": True,
        "status_id": item_data["status_id"],
        "video_game_rating_id": item_data["video_game_rating_id"],
        "price": item_data["price"]["amount"],
        "package_size_id": item_data["package_size_id"],
        "shipment_prices": {"domestic": None, "international": None},
        "color_ids": color_ids if color_ids else None,
        "assigned_photos": [],
        "measurement_length": item_data["measurement_length"],
        "measurement_width": item_data["measurement_width"],
        "item_attributes": item_data["item_attributes"],
    }


async def upload_photos(urls: List[str], temp_uuid: str, headers: dict) -> List[int]:
    """Uploads photos and returns list of photo IDs"""
    photo_ids = []

    for i, url in enumerate(urls):
        response = requests.get(url)
        if response.status_code != 200:
            continue

        files = [("photo[file]", (f"{i}.jpg", response.content, "image/jpeg"))]
        payload = {"photo[type]": "item", "photo[temp_uuid]": temp_uuid}

        response = requests.post(
            "https://www.vinted.fr/api/v2/photos",
            headers=headers,
            data=payload,
            files=files,
        )

        if response.status_code == 200:
            photo_ids.append(response.json()["id"])

    return photo_ids


@router.get("/refresh-ads")
async def refresh_ads(
    headers: dict = Depends(get_vinted_headers), session: Session = Depends(get_session)
):
    """Refreshes ads available for the authenticated profile"""
    same_row = 0
    page = 1

    while True:
        user = session.exec(select(User).where(User.id == 1)).first()
        url = f"{API_URL}wardrobe/{user.userId}/items?page={page}&per_page=20&order=revelance"
        response = execute_request("get", url, headers)

        if response.status_code != 200:
            break

        data = response.json()
        items = data["items"]

        if not items:
            break

        for item in items:

            if not (
                item["item_closing_action"] == None
                and item["is_reserved"] == False
                and item["is_closed"] == False
                and item["is_hidden"] == False
            ):
                continue

            continue

            # Prepare item data
            item_info = prepare_item_info(item)
            photo_urls = extract_photos_urls(item["photos"])

            # Handle rate limiting
            if same_row == 15:
                sleep(30)
                same_row = 0

            # Get temp UUID for upload
            response = requests.get("https://www.vinted.fr/items/new", headers=headers)
            temp_uuid = (
                re.search(
                    r'<div id="ItemUpload-react-component-\s*(.*?)\s*"',
                    response.text,
                    re.DOTALL,
                )
                .group(1)
                .strip()
            )

            # Upload photos
            photo_ids = await upload_photos(photo_urls, temp_uuid, headers)

            # Prepare final item data
            item_info["temp_uuid"] = temp_uuid
            item_info["assigned_photos"] = [
                {"id": pid, "orientation": 0} for pid in photo_ids
            ]

            # Upload item
            response = requests.post(
                "https://www.vinted.fr/api/v2/items",
                headers=headers,
                json={"item": item_info, "feedback_id": None},
            )

            if response.status_code == 200:
                # Delete old item
                requests.post(f"{API_URL}items/{item['id']}/delete", headers=headers)
                same_row += 1

        page += 1

    return {"message": "Ads refresh completed"}


@router.delete("/sold-items")
async def delete_sold_items(
    headers: dict = Depends(get_vinted_headers), session: Session = Depends(get_session)
):
    """Deletes all sold items"""
    page = 1

    while True:
        user = session.exec(select(User).where(User.id == 1)).first()
        url = f"{API_URL}wardrobe/{user.userId}/items?page={page}&per_page=20&order=revelance"
        response = execute_request("get", url, headers)
        nb_items_deleted = 0

        if response.status_code != 200:
            break

        data = response.json()
        items = data["items"]

        if not items:
            break

        for item in items:
            if not (
                item["item_closing_action"] == "sold" and item["is_closed"] == True
            ):
                continue

            if nb_items_deleted == 5:
                sleep(30)
                nb_items_deleted = 0

            response = execute_request(
                "delete", f"{API_URL}items/{item['id']}/delete", headers
            )
            if response.status_code == 200:
                nb_items_deleted += 1

        page += 1

    return {"message": "Sold items deleted"}


@router.delete("/all-ads")
async def delete_all_ads(
    headers: dict = Depends(get_vinted_headers), session: Session = Depends(get_session)
):
    """Deletes all ads"""
    page = 1

    while True:
        user = session.exec(select(User).where(User.id == 1)).first()
        url = f"{API_URL}wardrobe/{user.userId}/items?page={page}&per_page=20&order=revelance"
        response = execute_request("get", url, headers)
        nb_items_deleted = 0

        if response.status_code != 200:
            break

        data = response.json()
        items = data["items"]

        if not items:
            break

        for item in items:

            if nb_items_deleted == 5:
                sleep(30)
                nb_items_deleted = 0

            response = execute_request(
                "delete", f"{API_URL}items/{item['id']}/delete", headers
            )
            if response.status_code == 200:
                nb_items_deleted += 1

        page += 1

    return {"message": "All ads deleted"}
