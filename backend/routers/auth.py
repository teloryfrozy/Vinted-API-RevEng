import re
from fastapi import APIRouter
from pydantic import BaseModel
from sqlmodel import Session, select
from config.models import User, get_session
from fastapi import APIRouter, Depends

router = APIRouter(
    prefix="/auth",
)


class VintedToken(BaseModel):
    vintedAccessToken: str
    vintedRefreshToken: str


class Settings(BaseModel):
    userProfileURL: str | None = None
    language: str | None = None
    imapDomain: str | None = None
    imapPort: int | None = None
    imapUsername: str | None = None
    imapPassword: str | None = None


@router.post("/vinted-token")
async def save_vinted_token(
    vinted_token: VintedToken, session: Session = Depends(get_session)
):
    user = session.exec(select(User).where(User.id == 1)).first()

    if not user:
        user = User(
            id=1,
            vinted_access_token=(
                vinted_token.vintedAccessToken
                if vinted_token.vintedAccessToken
                else None
            ),
            vinted_refresh_token=(
                vinted_token.vintedRefreshToken
                if vinted_token.vintedRefreshToken
                else None
            ),
        )
    else:
        if vinted_token.vintedAccessToken:
            user.vinted_access_token = vinted_token.vintedAccessToken
        if vinted_token.vintedRefreshToken:
            user.vinted_refresh_token = vinted_token.vintedRefreshToken

    session.add(user)
    session.commit()

    return {"success": True}


@router.post("/settings")
async def save_settings(settings: Settings, session: Session = Depends(get_session)):
    user = session.exec(select(User).where(User.id == 1)).first()
    if not user:
        user = User(
            id=1,
            userId=int(re.search("\d+", settings.userProfileURL).group(0)),
        )
    else:
        user.userId = int(re.search("\d+", settings.userProfileURL).group(0))

    session.add(user)
    session.commit()

    return {"success": True}
