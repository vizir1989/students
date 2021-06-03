import os

import pytest

from tests.conftest import FAKE_TIME

dir_path = os.path.dirname(os.path.realpath(__file__))

TASK_FIXTURE = os.path.join(dir_path, 'fixture')


@pytest.mark.parametrize('fixtures_dir, token, expected_code, expected_result',
                         (
                                 [
                                     TASK_FIXTURE,
                                     'Bearer test1',
                                     200,
                                     {'articles': [{'author': {'bio': '',
                                                               'following': False,
                                                               'image': None,
                                                               'username': 'test1'},
                                                    'body': 'body 1',
                                                    'createdAt': FAKE_TIME,
                                                    'description': 'description 1',
                                                    'favorited': False,
                                                    'favoritesCount': 0,
                                                    'id': None,
                                                    'slug': 'title-1',
                                                    'tagList': ['tag 1', 'tag 2'],
                                                    'title': 'title 1',
                                                    'updatedAt': None},
                                                   {'author': {'bio': '',
                                                               'following': False,
                                                               'image': None,
                                                               'username': 'test1'},
                                                    'body': 'body 2',
                                                    'createdAt': FAKE_TIME,
                                                    'description': 'description 2',
                                                    'favorited': False,
                                                    'favoritesCount': 0,
                                                    'id': None,
                                                    'slug': 'title-2',
                                                    'tagList': ['tag 3', 'tag 2'],
                                                    'title': 'title 2',
                                                    'updatedAt': None},
                                                   {'author': {'bio': '',
                                                               'following': False,
                                                               'image': None,
                                                               'username': 'test1'},
                                                    'body': 'body 3',
                                                    'createdAt': FAKE_TIME,
                                                    'description': 'description 3',
                                                    'favorited': False,
                                                    'favoritesCount': 0,
                                                    'id': None,
                                                    'slug': 'title-3',
                                                    'tagList': ['tag 1', 'tag 5'],
                                                    'title': 'title 3',
                                                    'updatedAt': None}],
                                      'articlesCount': 3}
                                 ],
                                 [
                                     TASK_FIXTURE,
                                     'Bearer test2',
                                     404,
                                     {}
                                 ]
                         )
                         )
def test_get_articles(test_client, get_articles_fixture, token, expected_code,
                      expected_result):
    response = test_client.get(f'/api/v1/articles/feed', headers={'Authorization': token})
    assert response.status_code == expected_code
    if expected_result:
        assert response.json() == expected_result
