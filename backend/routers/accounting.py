import datetime
import re
from fastapi import HTTPException, APIRouter, Depends
from pydantic import BaseModel
from sqlmodel import Session, select
from constants import API_URL
from utils import execute_request, get_vinted_headers
from config.models import User, get_session
from fastapi import APIRouter, Depends

router = APIRouter(
    prefix="/accounting",
)


class CleanConversations(BaseModel):
    monthsToKeep: int


@router.post("/clean-conversations")
async def clean_conversations(
    clean_conversations: CleanConversations,
    session: Session = Depends(get_session),
    headers: dict = Depends(get_vinted_headers),
):
    page = 1
    nb_conversations_deleted = 0

    response = execute_request(
        "GET", f"{API_URL}inbox?page={page}?per_page=20", headers, session=session
    )

    total_pages = response.json()["pagination"]["total_pages"]

    while page < total_pages:
        response = execute_request(
            "GET", f"{API_URL}inbox?page={page}?per_page=20", headers, session=session
        )

        for conversation in response.json()["conversations"]:
            if (datetime.datetime.now() - datetime.datetime.strptime(conversation["updated_at"].split("+")[0], "%Y-%m-%dT%H:%M:%S")).days > clean_conversations.monthsToKeep * 30:
                nb_conversations_deleted += 1
                if not conversation["is_deletion_restricted"]:
                    execute_request(
                        "DELETE",
                        f"{API_URL}conversations/{conversation['id']}",
                        headers,
                        session=session,
                    )

        page += 1

    return {
        "message": "Conversations cleaned",
        "nnConversationsDeleted": nb_conversations_deleted,
    }
