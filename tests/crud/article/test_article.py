import os
from datetime import datetime, timezone
from typing import Union, Callable

import pytest
from bson import ObjectId
from motor.motor_asyncio import AsyncIOMotorClient

from app.core.config import database_name, Collection
from app.crud.article import is_article_favorited_by_user, add_article_to_favorites, remove_article_from_favorites, \
    get_favorites_count_for_article, get_article_by_slug

dir_path = os.path.dirname(os.path.realpath(__file__))

TASK_FIXTURE = os.path.join(dir_path, 'fixture')


@pytest.mark.parametrize('fixtures_dir, user, article, expected_exception, expected_result',
                         (
                                 [
                                     TASK_FIXTURE,
                                     'test1',
                                     'title-2',
                                     None,
                                     True,
                                 ],
                                 [
                                     TASK_FIXTURE,
                                     'test2',
                                     'title-2',
                                     None,
                                     False,
                                 ],
                                 [
                                     TASK_FIXTURE,
                                     'test3',
                                     'title-2',
                                     RuntimeError,
                                     None,
                                 ],
                                 [
                                     TASK_FIXTURE,
                                     'test2',
                                     'title-3',
                                     RuntimeError,
                                     None,
                                 ],
                                 [
                                     TASK_FIXTURE,
                                     'test3',
                                     'title-3',
                                     RuntimeError,
                                     None,
                                 ],
                         )
                         )
@pytest.mark.asyncio
async def test_is_article_favorited_by_user(test_conn: AsyncIOMotorClient,
                                            article_fixture: Callable,
                                            user: str, article: str,
                                            expected_exception: Union[Exception, None],
                                            expected_result: Union[bool, None]):
    result = None
    if expected_exception is not None:
        with pytest.raises(expected_exception):
            await is_article_favorited_by_user(test_conn, article, user)
    else:
        result = await is_article_favorited_by_user(test_conn, article, user)

    if expected_result is not None:
        assert result == expected_result


@pytest.mark.parametrize('fixtures_dir, user, article, expected_exception, expected_result',
                         (
                                 [
                                     TASK_FIXTURE,
                                     'test1',
                                     'title-2',
                                     None,
                                     2,
                                 ],
                                 [
                                     TASK_FIXTURE,
                                     'test2',
                                     'title-2',
                                     None,
                                     2,
                                 ],
                                 [
                                     TASK_FIXTURE,
                                     'test3',
                                     'title-2',
                                     RuntimeError,
                                     None,
                                 ],
                                 [
                                     TASK_FIXTURE,
                                     'test2',
                                     'title-3',
                                     RuntimeError,
                                     None,
                                 ],
                                 [
                                     TASK_FIXTURE,
                                     'test3',
                                     'title-3',
                                     RuntimeError,
                                     None,
                                 ],
                         )
                         )
@pytest.mark.asyncio
async def test_add_article_to_favorites(test_conn: AsyncIOMotorClient,
                                        article_fixture: Callable,
                                        user: str, article: str,
                                        expected_exception: Union[Exception, None],
                                        expected_result: Union[dict, None]):
    if expected_exception is not None:
        with pytest.raises(expected_exception):
            await add_article_to_favorites(test_conn, article, user)
    else:
        await add_article_to_favorites(test_conn, article, user)

    if expected_result is not None:
        result = await test_conn[database_name][Collection.favorites.value].count_documents({})
        assert result == expected_result


@pytest.mark.parametrize('fixtures_dir, user, article, expected_exception, expected_result',
                         (
                                 [
                                     TASK_FIXTURE,
                                     'test1',
                                     'title-2',
                                     None,
                                     0,
                                 ],
                                 [
                                     TASK_FIXTURE,
                                     'test2',
                                     'title-2',
                                     None,
                                     1,
                                 ],
                                 [
                                     TASK_FIXTURE,
                                     'test3',
                                     'title-2',
                                     RuntimeError,
                                     None,
                                 ],
                                 [
                                     TASK_FIXTURE,
                                     'test2',
                                     'title-3',
                                     RuntimeError,
                                     None,
                                 ],
                                 [
                                     TASK_FIXTURE,
                                     'test3',
                                     'title-3',
                                     RuntimeError,
                                     None,
                                 ],
                         )
                         )
@pytest.mark.asyncio
async def test_remove_article_from_favorites(test_conn: AsyncIOMotorClient,
                                             article_fixture: Callable,
                                             user: str, article: str,
                                             expected_exception: Union[Exception, None],
                                             expected_result: Union[dict, None]):
    if expected_exception is not None:
        with pytest.raises(expected_exception):
            await remove_article_from_favorites(test_conn, article, user)
    else:
        await remove_article_from_favorites(test_conn, article, user)

    if expected_result is not None:
        result = await test_conn[database_name][Collection.favorites.value].count_documents({})
        assert result == expected_result


@pytest.mark.parametrize('fixtures_dir, article, expected_exception, expected_result',
                         (
                                 [
                                     TASK_FIXTURE,
                                     'title-1',
                                     None,
                                     0,
                                 ],
                                 [
                                     TASK_FIXTURE,
                                     'title-2',
                                     None,
                                     1,
                                 ],
                                 [
                                     TASK_FIXTURE,
                                     'title-3',
                                     RuntimeError,
                                     None,
                                 ]
                         )
                         )
@pytest.mark.asyncio
async def test_get_favorites_count_for_article(test_conn: AsyncIOMotorClient,
                                               article_fixture: Callable,
                                               article: str,
                                               expected_exception: Union[Exception, None],
                                               expected_result: Union[dict, None]):
    result = None
    if expected_exception is not None:
        with pytest.raises(expected_exception):
            await get_favorites_count_for_article(test_conn, article)
    else:
        result = await get_favorites_count_for_article(test_conn, article)

    if expected_result is not None:
        assert result == expected_result


@pytest.mark.parametrize('fixtures_dir, user, article, expected_exception, expected_result',
                         (
                                 [
                                     TASK_FIXTURE,
                                     'test1',
                                     'title-1',
                                     None,
                                     {'title': 'title 1', 'description': 'description 1', 'body': 'body 1',
                                      'tagList': ['tag 1', 'tag 2'],
                                      'createdAt': datetime(2020, 1, 1, 0, 0, tzinfo=timezone.utc), 'slug': 'title-1',
                                      'author': {'username': 'test1', 'bio': '', 'image': None,
                                                 'following': False}, 'favorited': False,
                                      'favoritesCount': 0, '_id': ObjectId('111111111111111111111111')},
                                 ],
                                 [
                                     TASK_FIXTURE,
                                     'test1',
                                     'title-2',
                                     None,
                                     {'_id': ObjectId('111111111111111111111112'),
                                      'author': {'bio': '', 'following': False, 'image': None, 'username': 'test2'},
                                      'body': 'body 2',
                                      'createdAt': datetime(2020, 1, 1, 0, 0, tzinfo=timezone.utc),
                                      'description': 'description 2',
                                      'favorited': True,
                                      'favoritesCount': 1,
                                      'slug': 'title-2',
                                      'tagList': ['tag 1', 'tag 3'],
                                      'title': 'title 2'},
                                 ],
                                 [
                                     TASK_FIXTURE,
                                     'test3',
                                     'title-1',
                                     RuntimeError,
                                     None,
                                 ],
                                 [
                                     TASK_FIXTURE,
                                     'test1',
                                     'title-3',
                                     None,
                                     None,
                                 ],
                                 [
                                     TASK_FIXTURE,
                                     None,
                                     'title-2',
                                     RuntimeError,
                                     None,
                                 ]
                         )
                         )
@pytest.mark.asyncio
async def test_get_article_by_slug(test_conn: AsyncIOMotorClient,
                                   article_fixture: Callable,
                                   user: str, article: str,
                                   expected_exception: Union[Exception, None],
                                   expected_result: Union[dict, None]):
    result = None
    if expected_exception is not None:
        with pytest.raises(expected_exception):
            await get_article_by_slug(test_conn, article, user)
    else:
        result = await get_article_by_slug(test_conn, article, user)

    if expected_result is not None:
        result = result.mongo()
        assert result == expected_result
