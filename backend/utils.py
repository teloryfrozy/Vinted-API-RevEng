import datetime
import requests
from fastapi import HTTPException, Depends
from constants import API_URL, BASE_HEADERS
from sqlmodel import Session, select
from config.models import User, get_session


MAX_RETRIES = 3


def get_vinted_headers(session: Session = Depends(get_session)) -> dict:
    """Returns headers for Vinted API requests"""
    session = next(get_session())
    auth = session.exec(select(User).order_by(User.id.desc())).first()

    if not auth:
        raise HTTPException(
            status_code=401,
            detail="No Vinted authentication found. Please login first.",
        )

    headers = {
        **BASE_HEADERS,
        "Cookie": f"access_token_web={auth.vinted_access_token}; refresh_token_web={auth.vinted_refresh_token}",
    }

    if auth.expires_at and auth.expires_at < datetime.datetime.now():
        refresh_access_token(headers, session)
        auth = session.exec(select(User).order_by(User.id.desc())).first()

    i = 0

    while i < MAX_RETRIES:
        response = requests.get(f"{API_URL}users/countries", headers=headers)

        if response.status_code == 200:
            return headers

        refresh_access_token(headers, session)
        auth = session.exec(select(User).order_by(User.id.desc())).first()
        headers["Cookie"] = (
            f"access_token_web={auth.vinted_access_token}; refresh_token_web={auth.vinted_refresh_token}"
        )
        i += 1

    raise HTTPException(
        status_code=401,
        detail="Token refused by Vinted server. Please update your token.",
    )


def execute_request(
    method: str,
    url: str,
    headers: dict,
    data: dict = None,
    session: Session = Depends(get_session),
) -> requests.Response:
    i = 0

    while i < MAX_RETRIES:
        if method == "GET":
            response = requests.get(url, headers=headers)
        elif method == "POST":
            response = requests.post(url, headers=headers, json=data)
        elif method == "PATCH":
            response = requests.patch(url, headers=headers, json=data)
        elif method == "DELETE":
            response = requests.delete(url, headers=headers, json=data)

        if response.status_code != 200:
            refresh_access_token(headers, session)

            headers = get_vinted_headers(session)
            print(
                f"Status code: {response.status_code}",
                f"Reason: {response.reason}",
                f"data: {data}",
                f"url: {url}",
            )
            i += 1
        else:
            return response

    raise HTTPException(
        status_code=401,
        detail="Token refused by Vinted server. Please update your token.",
    )


def refresh_access_token(headers: dict, session: Session):
    response = requests.post(
        f"https://www.vinted.fr/web/api/auth/refresh", headers=headers
    )
    if response.status_code != 200:
        raise HTTPException(
            status_code=401,
            detail=f"Refresh token refused by Vinted server. Please update your token. Response: {response.text}",
        )
    # https://stackoverflow.com/questions/68981634/attributeerror-depends-object-has-no-attribute-query-fastapi
    session = next(get_session())
    auth = session.exec(select(User).order_by(User.id.desc())).first()
    auth.vinted_access_token = response.json()["access_token"]
    auth.vinted_refresh_token = response.json()["refresh_token"]
    session.add(auth)
    session.commit()
