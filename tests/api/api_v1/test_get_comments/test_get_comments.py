import os

import pytest

dir_path = os.path.dirname(os.path.realpath(__file__))

TASK_FIXTURE = os.path.join(dir_path, 'fixture')


@pytest.mark.parametrize('fixtures_dir, token, slug, expected_code, expected_result',
                         (
                                 [
                                     TASK_FIXTURE,
                                     'Bearer test1',
                                     'title-1',
                                     200,
                                     {'comments': [
                                         {'createdAt': None, 'updatedAt': None, 'id': '111111111111111111111111',
                                          'body': 'comment 1', 'author': {'username': 'test1', 'bio': '', 'image': None,
                                                                          'following': False}}]}
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
def test_get_comments(test_client, get_comments_fixture, token, slug, expected_code,
                      expected_result):
    response = test_client.get(f'/api/v1/articles/{slug}/comments', headers={'Authorization': token})
    assert response.status_code == expected_code
    if expected_result:
        assert response.json() == expected_result
