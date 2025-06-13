"""
TODO:
- add a input front to select the number of n last ads to refresh
- finish the refresh ads function
"""

import json
import requests
import re
from bs4 import BeautifulSoup
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


def prepare_item_info(item: dict) -> dict:
    pass


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

    url = f"{API_URL}wardrobe/4977264403/items?page={page}&per_page=20&order=revelance"
    response = execute_request("GET", url, headers)

    total_pages = response.json()["pagination"]["total_pages"]

    while page <= total_pages:
        user = session.exec(select(User).where(User.id == 1)).first()
        url = f"{API_URL}wardrobe/{user.userId}/items?page={page}&per_page=20&order=revelance"
        response = execute_request("GET", url, headers)

        data = response.json()
        items = data["items"]

        for item in items:
            if not (
                item["item_closing_action"] == None
                and item["is_draft"] == False
                and item["is_reserved"] == False
                and item["is_closed"] == False
                and item["is_hidden"] == False
            ):
                continue

            # Vinted uses SSR for item data so we need to scrap it from HTML
            path = item["path"]
            item_url = f"https://www.vinted.fr{path}"

            response = execute_request("GET", item_url, headers)

            result = re.search(
                r'(\{"itemDto":.*?"electronicsVerification":.*?\}\})\]',
                response.text.replace('\\"', '"').replace("\\\\n", "\\n"),
            )
            if result:
                item_dto_str = result.group(1)

                try:
                    item_data = json.loads(item_dto_str)
                except json.JSONDecodeError as e:
                    print(f"Error parsing JSON: {e}")
            else:
                print("No item data found in the response")

            return {
                "message": "Item data fetched successfully",
            }

            # Prepare item data
            # item_info = prepare_item_info(item)
            # photo_urls = extract_photos_urls(item["photos"])

            # # Handle rate limiting
            # if same_row == 15:
            #     sleep(30)
            #     same_row = 0

            # # Get temp UUID for upload
            # response = requests.get("https://www.vinted.fr/items/new", headers=headers)
            # temp_uuid = (
            #     re.search(
            #         r'<div id="ItemUpload-react-component-\s*(.*?)\s*"',
            #         response.text,
            #         re.DOTALL,
            #     )
            #     .group(1)
            #     .strip()
            # )

            # # Upload photos
            # photo_ids = await upload_photos(photo_urls, temp_uuid, headers)

            # # Prepare final item data
            # item_info["temp_uuid"] = temp_uuid
            # item_info["assigned_photos"] = [
            #     {"id": pid, "orientation": 0} for pid in photo_ids
            # ]

            # Upload item
            # response = requests.post(
            #     "https://www.vinted.fr/api/v2/items",
            #     headers=headers,
            #     json={"item": item_info, "feedback_id": None},
            # )

            # if response.status_code == 200:
            #     # Delete old item
            #     requests.post(f"{API_URL}items/{item['id']}/delete", headers=headers)
            #     same_row += 1

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
        response = execute_request("GET", url, headers)
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
        response = execute_request("GET", url, headers)
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
