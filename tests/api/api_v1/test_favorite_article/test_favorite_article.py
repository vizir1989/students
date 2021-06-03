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
                                     'title-2',
                                     200,
                                     {"article": {"title": "title 2", "description": "description 2", "body": "body 2",
                                                  "tagList": ["tag 1", "tag 3"], "createdAt": FAKE_TIME,
                                                  "updatedAt": None, "slug": "title-2",
                                                  "author": {"username": "test2", "bio": "", "image": None,
                                                             "following": False}, "favorited": True,
                                                  "favoritesCount": 1, "id": None}},
                                 ],
                                 [
                                     TASK_FIXTURE,
                                     'Bearer test2',
                                     'title-1',
                                     200,
                                     {"article": {"title": "title 1", "description": "description 1", "body": "body 1",
                                                  "tagList": ["tag 1", "tag 2"], "createdAt": FAKE_TIME,
                                                  "updatedAt": None, "slug": "title-1",
                                                  "author": {"username": "test1", "bio": "", "image": None,
                                                             "following": False}, "favorited": True,
                                                  "favoritesCount": 1, "id": None}},
                                 ]
                         )
                         )
def test_post_favorite_article(test_client, post_favorite_article, token, slug, expected_code,
                               expected_result):
    response = test_client.post(f'/api/v1/articles/{slug}/favorite', headers={'Authorization': token})
    assert response.status_code == expected_code
    if expected_result:
        assert response.json() == expected_result
