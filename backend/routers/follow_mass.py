import re
import requests
import time
from fastapi import HTTPException, APIRouter, Depends
from utils import get_vinted_headers
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
    response = requests.get(
        f"{API_URL}users/{user.userId}/followed_users?page={page}&per_page=20",
        headers=headers,
    )

    if not response.status_code == 200:
        raise HTTPException(status_code=401, detail="Vinted token expired")

    session.exec(delete(FollowedUser).where(FollowedUser.userId == user.userId))

    pagination = response.json()["pagination"]
    nb_pages = pagination["total_pages"]

    while page <= nb_pages:
        response = requests.get(
            f"{API_URL}users/{user.userId}/followed_users?page={page}&per_page=20",
            headers=headers,
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


def toggle_follow(user_id: int, headers: dict):
    url = f"{API_URL}followed_users/toggle"
    data = {"user_id": user_id}
    response = requests.post(url, headers=headers, json=data)
    return response.json()


@router.get("/recover-followed-users")
async def recover_followed_users(
    headers: dict = Depends(get_vinted_headers), session: Session = Depends(get_session)
):
    user = session.exec(select(User).where(User.id == 1)).first()
    followed_users = session.exec(
        select(FollowedUser).where(FollowedUser.userId == user.userId)
    ).all()

    long_pause = 0
    short_pause = 0

    if long_pause == 100:
        time.sleep(60)
        long_pause = 0
    if short_pause == 30:
        time.sleep(10)
        short_pause = 0

    for followed_user in followed_users:
        if long_pause == 10:
            time.sleep(60)
            long_pause = 0
        if short_pause == 5:
            time.sleep(10)
            short_pause = 0
        toggle_follow(followed_user.followedUserId, headers)
        long_pause += 1
        short_pause += 1

    return {"message": "Users followed recovered"}


@router.get("/scrap-vinted-user")
async def scrap_vinted_user(scrap_vinted_user: ScrapVintedUser):
    id = re.search("\d+", scrap_vinted_user.url_seller).group(0)

    if scrap_vinted_user.mode == "followers":
        ...

    if scrap_vinted_user.mode == "following":
        ...

    return {"message": "Users scraped from vinted user"}
