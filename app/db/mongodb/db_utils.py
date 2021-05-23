import logging

from motor.motor_asyncio import AsyncIOMotorClient
from app.core.config import MONGODB_URL, MONGO_MAX_CONNECTIONS_COUNT, MONGO_MIN_CONNECTIONS_COUNT
from .db import db


async def connect_to_mongo():
    logging.info("Connecting to db...")
    db.client = AsyncIOMotorClient(str(MONGODB_URL),
                                   maxPoolSize=MONGO_MAX_CONNECTIONS_COUNT,
                                   minPoolSize=MONGO_MIN_CONNECTIONS_COUNT)
    logging.info("Connected to db!！")


async def close_mongo_connection():
    logging.info("Closing db...")
    db.client.close()
    logging.info("db closed!！")
