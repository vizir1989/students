import json
from os import walk, path

import datetime

import motor
import pymongo
import uuid
from pytest import fixture
from starlette.config import environ
from starlette.testclient import TestClient

from app.core.config import database_name, Collection
from app.db.mongodb.db import get_database


FAKE_TIME = datetime.datetime(2020, 1, 1, 0, 0, 0).strftime("%Y-%m-%dT%H:%M:%S%ZZ")


def find_all(collection_name, collection_filter):
    import asyncio

    loop = asyncio.get_event_loop()
    db = loop.run_until_complete(get_database())

    return loop.run_until_complete(find_all_function(db, collection_name, collection_filter))


async def find_all_function(db, collection_name, collection_filter):
    result = []
    cursor = db[database_name][collection_name].find(collection_filter)
    for item in await cursor.to_list(length=100):
        result.append(item)
    return result


@fixture(scope='function')
def test_client():
    from app.main import app
    with TestClient(app) as test_client:
        return test_client


@fixture(scope='function')
def mongo_load_fixture(test_client, fixtures_dir):
    try:
        import asyncio
        loop = asyncio.get_event_loop()
        db = loop.run_until_complete(get_database())
        for (dirpath, _, filenames) in walk(fixtures_dir):
            for filename in filenames:
                with open(path.join(dirpath, filename)) as fixture_file:
                    collection_name = path.splitext(filename)[0]
                    collection = json.load(fixture_file)
                    loop.run_until_complete(db[database_name][collection_name].insert_many(collection))
        yield

    finally:
        for collection_name in Collection:
            loop.run_until_complete(db[database_name][collection_name.value].drop())


@fixture(scope='function')
def create_user_fixture(mongo_load_fixture):
    pass


@fixture(scope='function')
def patch_verify_password(monkeypatch):
    def unhashed_check_password(instance, password):
        return instance.hashed_password == password

    monkeypatch.setattr('app.models.user.UserInDB.check_password', unhashed_check_password)


@fixture(scope='function')
def users_login_fixture(mongo_load_fixture, patch_verify_password):
    pass


@fixture(scope='function')
def patch_jwt_decode(monkeypatch):
    def mocked_decode(token, *args, **kwargs):
        return {'username': token}

    monkeypatch.setattr('jwt.decode', mocked_decode)


@fixture(scope='function')
def generation_time_mock(monkeypatch, mocker):
    property_mock = mocker.PropertyMock(return_value=FAKE_TIME)
    monkeypatch.setattr('bson.objectid.ObjectId.generation_time', property_mock)


@fixture(scope='function')
def create_new_article_fixture(mongo_load_fixture, patch_jwt_decode):
    pass


@fixture(scope='function')
def delete_article_fixture(mongo_load_fixture, patch_jwt_decode, generation_time_mock):
    pass


@fixture(scope='function')
def update_article_fixture(mongo_load_fixture, patch_jwt_decode):
    pass


@fixture(scope='function')
def get_article_fixture(mongo_load_fixture, patch_jwt_decode, generation_time_mock):
    pass


@fixture(scope='function')
def get_articles_fixture(mongo_load_fixture, patch_jwt_decode, generation_time_mock):
    pass


@fixture(scope='function')
def post_favorite_article_fixture(mongo_load_fixture, patch_jwt_decode, generation_time_mock):
    pass


@fixture(scope='function')
def delete_favorite_article_fixture(mongo_load_fixture, patch_jwt_decode, generation_time_mock):
    pass


@fixture(scope='function')
def get_comments_fixture(mongo_load_fixture, patch_jwt_decode, generation_time_mock):
    pass


@fixture(scope='function')
def create_comments_fixture(mongo_load_fixture, patch_jwt_decode, generation_time_mock):
    pass


@fixture(scope='function')
def get_user_feed_fixture(mongo_load_fixture, patch_jwt_decode, generation_time_mock):
    pass


# This line would raise an error if we use it after 'settings' has been imported.
environ['TESTING'] = 'TRUE'
