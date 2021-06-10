from app.db.mongodb.db import AsyncIOMotorClient
from pydantic import EmailStr
from bson.objectid import ObjectId

from app.core.config import database_name, Collection
from app.models.user import UserInCreate, UserInDB, UserInUpdate


async def get_user(conn: AsyncIOMotorClient, username: str) -> UserInDB:
    row = await conn[database_name][Collection.users.value].find_one({"username": username})
    if row:
        return UserInDB.from_mongo(row)


async def get_user_by_email(conn: AsyncIOMotorClient, email: EmailStr) -> UserInDB:
    row = await conn[database_name][Collection.users.value].find_one({"email": email})
    if row:
        return UserInDB.from_mongo(row)


async def create_user(conn: AsyncIOMotorClient, user: UserInCreate) -> UserInDB:
    dbuser = UserInDB.from_mongo(user.dict())
    dbuser.change_password(user.password)

    row = await conn[database_name][Collection.users.value].insert_one(dbuser.dict())

    dbuser.id = row.inserted_id
    dbuser.created_at = ObjectId(dbuser.id).generation_time
    dbuser.updated_at = ObjectId(dbuser.id).generation_time

    return dbuser


async def update_user(conn: AsyncIOMotorClient, username: str, user: UserInUpdate) -> UserInDB:
    dbuser = await get_user(conn, username)

    dbuser.username = user.username or dbuser.username
    dbuser.email = user.email or dbuser.email
    dbuser.bio = user.bio or dbuser.bio
    dbuser.image = user.image or dbuser.image
    if user.password:
        dbuser.change_password(user.password)

    updated_at = await conn[database_name][Collection.users.value]\
        .update_one({"username": dbuser.username}, {'$set': dbuser.dict()})
    dbuser.updated_at = updated_at
    return dbuser
