from motor.motor_asyncio import AsyncIOMotorClient
from pytest import fixture

from app.core.config import MONGODB_URL, MONGO_MAX_CONNECTIONS_COUNT, MONGO_MIN_CONNECTIONS_COUNT, Collection, \
    database_name


@fixture(scope='function')
def test_conn() -> AsyncIOMotorClient:
    try:
        client = AsyncIOMotorClient(str(MONGODB_URL),
                                    maxPoolSize=MONGO_MAX_CONNECTIONS_COUNT,
                                    minPoolSize=MONGO_MIN_CONNECTIONS_COUNT)
        yield client
        client.close()
    finally:
        import asyncio
        loop = asyncio.get_event_loop()
        client = AsyncIOMotorClient(str(MONGODB_URL),
                                    maxPoolSize=MONGO_MAX_CONNECTIONS_COUNT,
                                    minPoolSize=MONGO_MIN_CONNECTIONS_COUNT)
        for collection_name in Collection:
            loop.run_until_complete(client[database_name][collection_name.value].drop())


@fixture(scope='function')
def article_fixture(mongo_load_fixture, generation_time_mock):
    pass
