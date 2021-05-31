import os

import pytest

from tests.conftest import FAKE_TIME

dir_path = os.path.dirname(os.path.realpath(__file__))

TASK_FIXTURE = os.path.join(dir_path, 'fixture')


@pytest.mark.parametrize('fixtures_dir, token, slug, expected_code, expected_result',
                         (
                                 [
                                     TASK_FIXTURE,
                                     'Bearer test1',
                                     'title-1',
                                     200,
                                     {"article": {"title": "title 1", "description": "description 1", "body": "body 1",
                                                  "tagList": ["tag 1", "tag 2"], "createdAt": FAKE_TIME,
                                                  "updatedAt": None, "slug": "title-1",
                                                  "author": {"username": "test1", "bio": "", "image": None,
                                                             "following": False}, "favorited": False,
                                                  "favoritesCount": 0, "id": None}},
                                 ],
                                 [
                                     TASK_FIXTURE,
                                     'Bearer test1',
                                     'title-2',
                                     404,
                                     {}
                                 ],
                                 [
                                     TASK_FIXTURE,
                                     'Bearer test2',
                                     'title-1',
                                     404,
                                     {}
                                 ]
                         )
                         )
def test_get_article(test_client, get_article_fixture, token, slug, expected_code,
                     expected_result):
    response = test_client.get(f'/api/v1/articles/{slug}', headers={'Authorization': token})
    assert response.status_code == expected_code
    if expected_result:
        assert response.json() == expected_result
