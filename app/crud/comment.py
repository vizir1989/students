from typing import List, Optional

from starlette.exceptions import HTTPException
from starlette.status import HTTP_404_NOT_FOUND

from app.models.comment import CommentInCreate, CommentInDB
from app.db.mongodb.db import AsyncIOMotorClient
from app.core.config import Collection, database_name
from .profile import get_profile_for_user


async def get_comments_for_article(
    conn: AsyncIOMotorClient, slug: str, username: Optional[str] = None
) -> List[CommentInDB]:
    comments: List[CommentInDB] = []
    rows = conn[database_name][Collection.comments.value].find({"slug": slug, "username": username})
    async for row in rows:
        author = await get_profile_for_user(conn, row["username"], username)
        row['author'] = author
        comments.append(CommentInDB.from_mongo(row))
    return comments


async def create_comment(
    conn: AsyncIOMotorClient, slug: str, comment: CommentInCreate, username: str
) -> CommentInDB:
    comment_doc = comment.dict()
    comment_doc["slug"] = slug
    comment_doc["username"] = username
    await conn[database_name][Collection.comments.value].insert_one(comment_doc)
    author = await get_profile_for_user(conn, username, "")
    comment_doc['author'] = author
    return CommentInDB.from_mongo(comment_doc)


async def delete_comment_or_404(conn: AsyncIOMotorClient, id: str, username: str):
    result = await conn[database_name][Collection.comments.value].delete_many({"_id": id, "username": username})
    if result.deleted_count == 0:
        raise HTTPException(
            status_code=HTTP_404_NOT_FOUND,
            detail=f"Comments with id '{id}' not found",
        )