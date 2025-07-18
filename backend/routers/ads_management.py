"""
Notes:
- Vinted uses SSR and item data is hidden in html, its a pain to extract and I did not manage
They are building an API for pro users: https://pro-docs.svc.vinted.com/#vinted-pro-integrations-documentation-items-api
"""

import json
import requests
import re
from time import sleep
from fastapi import APIRouter, Depends
from utils import execute_request, get_vinted_headers
from constants import API_URL
from sqlmodel import Session, select
from config.models import User, get_session

router = APIRouter(
    prefix="/ads-management",
)


@router.get("/refresh-ads")
async def refresh_ads(
    headers: dict = Depends(get_vinted_headers), session: Session = Depends(get_session)
):
    """Refreshes ads available for the authenticated profile"""
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

            item_data = extract_item_json(response.text)

            if item_data:
                return {"message": "Not implemented"}

                """
                Roadmap to repost an item:
                1) Download current photos
                2) Upload new photos
                3) Delete item
                4) Upload item
                """

                # 3) Delete item before reposting it
                if delete_item(item["path"], item["id"], headers):
                    print(f"Item: {item_data['title']} deleted successfully")
                else:
                    print(f"Item: {item_data['title']} not deleted, skipping")
                    continue

                # 4) Upload item

                print(f"Item: {item_data['title']} reposted successfully")
            else:
                print("No item data found in the response, skipping")
                continue

        page += 1

    return {"message": "Ads refresh completed"}


@router.delete("/sold-items")
async def delete_sold_items(
    headers: dict = Depends(get_vinted_headers), session: Session = Depends(get_session)
):
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

            if delete_item(item["path"], item["id"], headers):
                nb_items_deleted += 1

        page += 1

    return {"message": "Sold items deleted"}


@router.delete("/all-ads")
async def delete_all_ads(
    headers: dict = Depends(get_vinted_headers), session: Session = Depends(get_session)
):
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

            if delete_item(item["path"], item["id"], headers):
                nb_items_deleted += 1

        page += 1

    return {"message": "All ads deleted"}


def delete_item(path: str, item_id: int, headers: dict) -> bool:
    item_url = f"https://www.vinted.fr{path}"

    csrf_token = get_csrf_token(item_url, headers)
    if csrf_token:
        headers["X-CSRF-Token"] = csrf_token
        response = execute_request(
            "DELETE", f"{API_URL}items/{item_id}/delete", headers
        )
        return response.status_code == 200
    else:
        return False


def get_csrf_token(item_url: str, headers: dict) -> str | None:
    response = requests.get(item_url, headers=headers)

    if response.status_code == 200:
        html_content = response.text
        pattern = r'\\"CSRF_TOKEN\\":\\"(.*?)\\"'

        matches = re.findall(pattern, html_content)
        if matches:
            return matches[0]
        return None
    else:
        return None


def extract_item_json(html_content: str):
    """Vinted loves to hide its data in html, this is how to extract with chatGPT"""
    # Find all script tags with the pattern
    script_matches = re.findall(
        r'self\.__next_f\.push\(\[1,"(.*?)"\]\)</script>', html_content, re.DOTALL
    )

    for json_str in script_matches:
        if json_str.startswith("16:"):
            json_str = json_str[3:]

        json_str = json_str.replace('\\"', '"').replace("\\\\n", "\\n")

        # Check if this script contains item_closing_action
        if "item_closing_action" in json_str:
            # Find the first complete JSON object
            brace_count = 0
            start = json_str.find("{")
            if start != -1:
                for i in range(start, len(json_str)):
                    if json_str[i] == "{":
                        brace_count += 1
                    elif json_str[i] == "}":
                        brace_count -= 1
                        if brace_count == 0:
                            json_str = json_str[start : i + 1]
                            break

            try:
                data = json.loads(json_str)

                # Find item in the structure
                def find_item(obj):
                    if isinstance(obj, dict) and "item" in obj:
                        return obj["item"]
                    elif isinstance(obj, dict):
                        for v in obj.values():
                            result = find_item(v)
                            if result:
                                return result
                    elif isinstance(obj, list):
                        for v in obj:
                            result = find_item(v)
                            if result:
                                return result
                    return None

                return find_item(data)
            except json.JSONDecodeError as e:
                print(f"Error parsing JSON: {e}")
                continue

    print("No script with item_closing_action found")
    return None
