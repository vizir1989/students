import os

import pytest

dir_path = os.path.dirname(os.path.realpath(__file__))

TASK_FIXTURE = os.path.join(dir_path, 'fixture')


@pytest.mark.parametrize('fixtures_dir, token, slug, comment, expected_code, expected_result',
                         (
                                 [
                                     TASK_FIXTURE,
                                     'Bearer test1',
                                     'title-1',
                                     {'comment': {'body': 'comment 1'}},
                                     201,
                                     {'comment': {'author': {'bio': '',
                                                             'following': False,
                                                             'image': None,
                                                             'username': 'test1'},
                                                  'body': 'comment 1',
                                                  'createdAt': None,
                                                  'id': None,
                                                  'updatedAt': None}}
                                 ],
                                 [
                                     TASK_FIXTURE,
                                     'Bearer test1',
                                     'title-2',
                                     {'comment': {'body': 'comment 1'}},
                                     404,
                                     {}
                                 ],
                                 [
                                     TASK_FIXTURE,
                                     'Bearer test2',
                                     'title-1',
                                     {'comment': {'body': 'comment 1'}},
                                     404,
                                     {}
                                 ]
                         )
                         )
def test_create_comments(test_client, create_comments_fixture, token, slug, comment, expected_code,
                         expected_result):
    response = test_client.post(f'/api/v1/articles/{slug}/comments', headers={'Authorization': token}, json=comment)
    assert response.status_code == expected_code
    if expected_result:
        assert response.json() == expected_result
