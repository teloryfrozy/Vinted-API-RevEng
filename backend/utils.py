import datetime
import requests
from fastapi import HTTPException, Depends
from constants import API_URL, BASE_HEADERS
from sqlmodel import Session, select
from config.models import User, get_session


def get_vinted_headers(session: Session = Depends(get_session)) -> dict:
    """Returns headers for Vinted API requests"""
    auth = session.exec(select(User).order_by(User.id.desc())).first()

    if not auth:
        raise HTTPException(
            status_code=401,
            detail="No Vinted authentication found. Please login first.",
        )

    if auth.expires_at and auth.expires_at < datetime.datetime.now():
        raise HTTPException(
            status_code=401, detail="Vinted token has expired. Please login again."
        )

    return {
        **BASE_HEADERS,
        "Cookie": f"access_token_web={auth.vinted_access_token}; refresh_token_web={auth.vinted_refresh_token}",
    }


def validate_vinted_token(session: Session = Depends(get_session)) -> str:
    """Validates the Vinted token from database"""
    auth = session.exec(select(User).order_by(User.id.desc())).first()

    if not auth:
        raise HTTPException(
            status_code=401,
            detail="No Vinted authentication found. Please login first.",
        )

    if auth.expires_at and auth.expires_at < datetime.datetime.now():
        raise HTTPException(
            status_code=401, detail="Vinted token has expired. Please login again."
        )

    headers = get_vinted_headers(auth.vinted_access_token, auth.vinted_refresh_token)
    response = requests.get(f"{API_URL}users/countries", headers=headers)

    if response.status_code != 200:
        raise HTTPException(
            status_code=401,
            detail="Token refused by Vinted server. Please update your token.",
        )

    return auth.vinted_access_token
