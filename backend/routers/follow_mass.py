import re
import time
from fastapi import HTTPException, APIRouter, Depends
from utils import execute_request, get_vinted_headers
from constants import API_URL
from sqlmodel import Session, select, delete
from config.models import FollowedUser, User, get_session
from pydantic import BaseModel

router = APIRouter(
    prefix="/follow-mass",
)


class ScrapVintedUser(BaseModel):
    urlSeller: str
    mode: str


@router.get("/backup-followed-users")
async def backup_followed_users(
    headers: dict = Depends(get_vinted_headers), session: Session = Depends(get_session)
):
    user = session.exec(select(User).where(User.id == 1)).first()
    page = 1
    response = execute_request(
        "get",
        f"{API_URL}users/{user.userId}/followed_users?page={page}&per_page=20",
        headers,
    )

    if not response.status_code == 200:
        raise HTTPException(status_code=401, detail="Vinted token expired")

    session.exec(delete(FollowedUser).where(FollowedUser.userId == user.userId))

    pagination = response.json()["pagination"]
    nb_pages = pagination["total_pages"]

    while page <= nb_pages:
        response = execute_request(
            "get",
            f"{API_URL}users/{user.userId}/followed_users?page={page}&per_page=20",
            headers,
        )
        for user_followed in response.json()["users"]:
            followed_user = session.exec(
                select(FollowedUser).where(
                    FollowedUser.followedUserId == user_followed["id"]
                )
            ).first()
            if not followed_user:
                followed_user = FollowedUser(
                    userId=user.userId, followedUserId=user_followed["id"]
                )
                session.add(followed_user)
        page += 1

    session.commit()

    return {"message": "Users followed backuped"}


def toggle_follow(user_id: int, headers: dict) -> int:
    url = f"{API_URL}followed_users/toggle"
    data = {"user_id": user_id}
    response = execute_request("POST", url, headers, data)
    print(
        f"[RESULT] user_id: {user_id} CODE: {response.status_code} | REASON: {response.reason} | text: {response.text}"
    )
    return response.status_code


@router.get("/recover-followed-users")
async def recover_followed_users(
    headers: dict = Depends(get_vinted_headers), session: Session = Depends(get_session)
):
    user = session.exec(select(User).where(User.id == 1)).first()

    nb_users_unfollowed = unfollow_all_users(user.userId, headers)
    nb_users_recovered = follow_all_users(user.userId, session, headers)

    return {
        "message": "Users followed recovered",
        "nbUsersUnfollowed": nb_users_unfollowed,
        "nbUsersRecovered": nb_users_recovered,
    }


def unfollow_all_users(user_id: int, headers: dict) -> int:
    nb_users_unfollowed = 0
    page = 1
    long_pause = 0
    short_pause = 0

    response = execute_request(
        "get",
        f"{API_URL}users/{user_id}/following?page={page}&per_page=20",
        headers=headers,
    )
    nb_pages = response.json()["pagination"]["total_pages"]

    while page <= nb_pages:

        if long_pause == 100:
            time.sleep(60)
            long_pause = 0
        if short_pause == 30:
            time.sleep(10)
            short_pause = 0

        response = execute_request(
            "get",
            f"{API_URL}users/{user_id}/following?page={page}&per_page=20",
            headers=headers,
        )

        for user in response.json()["users"]:
            status_code = toggle_follow(user["id"], headers)

            if status_code == 200:
                nb_users_unfollowed += 1

            long_pause += 1
            short_pause += 1

        page += 1

    return nb_users_unfollowed


def follow_all_users(user_id: int, session: Session, headers: dict) -> int:
    followed_users = session.exec(
        select(FollowedUser).where(FollowedUser.userId == user_id)
    ).all()

    long_pause = 0
    short_pause = 0
    nb_users_recovered = 0

    for followed_user in followed_users:
        if long_pause == 10:
            time.sleep(60)
            long_pause = 0
        if short_pause == 5:
            time.sleep(10)
            short_pause = 0

        status_code = toggle_follow(followed_user.followedUserId, headers)

        if status_code == 200:
            nb_users_recovered += 1

        long_pause += 1
        short_pause += 1


@router.post("/scrap-vinted-user")
async def scrap_vinted_user(
    scrap_vinted_user: ScrapVintedUser, headers: dict = Depends(get_vinted_headers)
):
    id = re.search("\d+", scrap_vinted_user.urlSeller).group(0)
    page = 1
    nb_users_scraped = 0
    mode = "followers" if scrap_vinted_user.mode == "followers" else "following"

    response = execute_request(
        "get",
        f"{API_URL}users/{id}/{mode}?page={page}&per_page=20",
        headers=headers,
    )
    nb_pages = response.json()["pagination"]["total_pages"]

    while page <= nb_pages:
        response = execute_request(
            "get",
            f"{API_URL}users/{id}/{mode}?page={page}&per_page=20",
            headers=headers,
        )

        for user in response.json()["users"]:
            print(f"Scraping user: {user['login']} | id: {user['id']}")

            if user["is_favourite"] == False and user["id"] != id:
                status_code = toggle_follow(user["id"], headers)
                if status_code == 200:
                    nb_users_scraped += 1

        page += 1

    return {
        "message": "Users scraped from vinted user",
        "nbUsersScraped": nb_users_scraped,
    }
