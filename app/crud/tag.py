from typing import List

from app.db.mongodb.db import AsyncIOMotorClient
from app.models.tag import Tag
from app.core.config import database_name, tags_collection_name, article_collection_name


async def fetch_all_tags(conn: AsyncIOMotorClient) -> List[Tag]:
    tags = []
    rows = conn[database_name][tags_collection_name].find()
    async for row in rows:
        tags.append(Tag(**row))

    return tags


async def get_tags_for_article(conn: AsyncIOMotorClient, slug: str) -> List[Tag]:
    tags = []
    article_tags = await conn[database_name][article_collection_name].find_one({"slug": slug},
                                                                               projection={"tag_list": True})
    for row in article_tags["tag_list"]:
        tags.append(Tag(tag=row))

    return tags


async def create_tags_that_not_exist(conn: AsyncIOMotorClient, tags: List[str]):
    await conn[database_name][tags_collection_name].insert_many([{"tag": tag} for tag in tags])