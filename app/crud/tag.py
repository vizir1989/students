from typing import List

from app.core.config import database_name, Collection
from app.db.mongodb.db import AsyncIOMotorClient
from app.models.tag import Tag


async def fetch_all_tags(conn: AsyncIOMotorClient) -> List[Tag]:
    tags = []
    rows = conn[database_name][Collection.tags.value].find()
    async for row in rows:
        tags.append(Tag(**row))

    return tags


async def get_tags_for_article(conn: AsyncIOMotorClient, slug: str) -> List[Tag]:
    tags = []
    article_tags = await conn[database_name][Collection.article.value].find_one({"slug": slug},
                                                                          projection={"tag_list": True})
    for row in article_tags["tag_list"]:
        tags.append(Tag(tag=row))

    return tags


async def create_tags_that_not_exist(conn: AsyncIOMotorClient, tags: List[str]):
    await conn[database_name][Collection.tags.value].insert_many([{"tag": tag} for tag in tags])
