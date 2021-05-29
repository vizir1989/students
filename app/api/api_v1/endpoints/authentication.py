from datetime import timedelta

from fastapi import APIRouter, Body, Depends
from fastapi.security import OAuth2PasswordRequestForm
from starlette.exceptions import HTTPException
from starlette.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST

from app.core.config import ACCESS_TOKEN_EXPIRE_MINUTES
from app.core.jwt import create_access_token
from app.crud.shortcuts import check_free_username_and_email
from app.crud.user import create_user, get_user_by_email, get_user
from app.db.mongodb.db import AsyncIOMotorClient, get_database
from app.models.user import User, UserInCreate, UserInLogin, UserInResponse, UserWithToken

router = APIRouter()


@router.post("/users/login", response_model=UserWithToken, tags=["authentication"])
async def login(
        form_data: OAuth2PasswordRequestForm = Depends(), db: AsyncIOMotorClient = Depends(get_database)
):
    dbuser = await get_user(db, form_data.username)
    if not dbuser or not dbuser.check_password(form_data.password):
        raise HTTPException(
            status_code=HTTP_400_BAD_REQUEST, detail="Incorrect user name or password"
        )

    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    token = create_access_token(
        data={"username": dbuser.username}, expires_delta=access_token_expires
    )
    return UserWithToken(user=User(**dbuser.dict()), access_token=token, token_type='Bearer')


@router.post(
    "/users",
    response_model=UserInResponse,
    tags=["authentication"],
    status_code=HTTP_201_CREATED,
)
async def register(
        user: UserInCreate = Body(..., embed=True), db: AsyncIOMotorClient = Depends(get_database)
):
    await check_free_username_and_email(db, user.username, user.email)

    async with await db.start_session() as s:
        async with s.start_transaction():
            dbuser = await create_user(db, user)
            access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
            token = create_access_token(
                data={"username": dbuser.username}, expires_delta=access_token_expires
            )

            return UserInResponse(user=User(**dbuser.dict(), token=token))