import os

import pytest

dir_path = os.path.dirname(os.path.realpath(__file__))

TASK_FIXTURE = os.path.join(dir_path, 'fixture')


@pytest.mark.parametrize('fixtures_dir, token, filter, expected_code, expected_result',
                         (
                                 [
                                     TASK_FIXTURE,
                                     'Bearer test1',
                                     {
                                         'tag': 'tag 1'
                                     },
                                     200,
                                     {"articles": [
                                         {"title": "title 1", "description": "description 1", "body": "body 1",
                                          "tagList": ["tag 1", "tag 2"], "createdAt": "2020-01-01T00:00:00Z",
                                          "updatedAt": None, "slug": "title-1",
                                          "author": {"username": "test1", "bio": "", "image": None, "following": False},
                                          "favorited": False, "favoritesCount": 0, "id": None}], "articlesCount": 1}
                                 ],
                                 [
                                     TASK_FIXTURE,
                                     'Bearer test1',
                                     {
                                         'author_id': 'test1'
                                     },
                                     200,
                                     {"articles": [
                                         {"title": "title 1", "description": "description 1", "body": "body 1",
                                          "tagList": ["tag 1", "tag 2"], "createdAt": "2020-01-01T00:00:00Z",
                                          "updatedAt": None, "slug": "title-1",
                                          "author": {"username": "test1", "bio": "", "image": None, "following": False},
                                          "favorited": False, "favoritesCount": 0, "id": None}], "articlesCount": 1},
                                 ],
                                 [
                                     TASK_FIXTURE,
                                     'Bearer test1',
                                     {
                                         'favorited': 'title-1'
                                     },
                                     200,
                                     {"articles": [
                                         {"title": "title 1", "description": "description 1", "body": "body 1",
                                          "tagList": ["tag 1", "tag 2"], "createdAt": "2020-01-01T00:00:00Z",
                                          "updatedAt": None, "slug": "title-1",
                                          "author": {"username": "test1", "bio": "", "image": None, "following": False},
                                          "favorited": False, "favoritesCount": 0, "id": None}], "articlesCount": 1},
                                 ],
                                 [
                                     TASK_FIXTURE,
                                     'Bearer test1',
                                     {
                                     },
                                     200,
                                     {"articles": [
                                         {"title": "title 1", "description": "description 1", "body": "body 1",
                                          "tagList": ["tag 1", "tag 2"], "createdAt": "2020-01-01T00:00:00Z",
                                          "updatedAt": None, "slug": "title-1",
                                          "author": {"username": "test1", "bio": "", "image": None, "following": False},
                                          "favorited": False, "favoritesCount": 0, "id": None}], "articlesCount": 1},
                                 ],
                                 [
                                     TASK_FIXTURE,
                                     'Bearer test1',
                                     {
                                         'tag': 'tag 3'
                                     },
                                     200,
                                     {'articles': [], 'articlesCount': 0},
                                 ],
[
                                     TASK_FIXTURE,
                                     '',
                                     {
                                         'tag': 'tag 1'
                                     },
                                     200,
                                     {"articles": [
                                         {"title": "title 1", "description": "description 1", "body": "body 1",
                                          "tagList": ["tag 1", "tag 2"], "createdAt": "2020-01-01T00:00:00Z",
                                          "updatedAt": None, "slug": "title-1",
                                          "author": {"username": "test1", "bio": "", "image": None, "following": False},
                                          "favorited": False, "favoritesCount": 0, "id": None}], "articlesCount": 1}
                                 ]
                         )
                         )
def test_get_articles(test_client, get_articles_fixture, token, filter, expected_code,
                      expected_result):
    if token:
        response = test_client.get(f'/api/v1/articles', headers={'Authorization': token}, params=filter)
    else:
        response = test_client.get(f'/api/v1/articles', params=filter)
    assert response.status_code == expected_code
    if expected_result:
        assert response.json() == expected_result
