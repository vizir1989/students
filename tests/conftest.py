from pytest import fixture
from starlette.config import environ
from starlette.testclient import TestClient
from app.db.mongodb.db import get_database
from app.core import config
from app.core.config import database_name, users_collection_name


@fixture(scope="function")
def test_user():
    return {
        "user": {
            "email": "user1@example.com",
            "password": "string1",
            "username": "string1"
        }
    }


@fixture(scope="function")
def test_database(monkeypatch):
    monkeypatch.setattr(config, 'database_name', 'test_fastapi')


@fixture(scope="function")
def test_client(test_user, test_database):
    from app.main import app
    test = database_name
    with TestClient(app) as test_client:
        yield test_client

    import asyncio
    db = asyncio.run(get_database())
    db[database_name][users_collection_name].delete_one({"username": test_user["user"]["username"]})


# This line would raise an error if we use it after 'settings' has been imported.
environ['TESTING'] = 'TRUE'
