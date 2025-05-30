from fastapi import FastAPI
from contextlib import asynccontextmanager
from sqlmodel import Field, Session, SQLModel, create_engine
from .settings import sqlite_url, connect_args
from datetime import datetime


ENGINE = create_engine(sqlite_url, connect_args=connect_args)


def create_db_and_tables():
    SQLModel.metadata.create_all(ENGINE)


def get_session():
    with Session(ENGINE) as session:
        yield session


@asynccontextmanager
async def lifespan(app: FastAPI):
    # stuff before app startup
    create_db_and_tables()
    yield
    # stuff after app shutdown


class FollowedUser(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    userId: int | None = Field(foreign_key="user.id")
    followedUserId: int | None = Field()


class User(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    vinted_access_token: str | None = Field()
    vinted_refresh_token: str | None = Field()
    expires_at: datetime | None = Field()
    imapDomain: str | None = Field()
    imapPort: int | None = Field()
    imapUsername: str | None = Field()
    imapPassword: str | None = Field()
    userId: int | None = Field()
