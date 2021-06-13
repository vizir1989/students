import os

import pytest

dir_path = os.path.dirname(os.path.realpath(__file__))

TASK_FIXTURE = os.path.join(dir_path, 'fixture')


@pytest.mark.parametrize('fixtures_dir, token, username, expected_code, expected_result',
                         (
                                 [
                                     TASK_FIXTURE,
                                     'Bearer test1',
                                     'test1',
                                     200,
                                     {'profile': {'bio': '', 'following': False, 'image': None, 'username': 'test1'}}
                                 ],
                                 [
                                     TASK_FIXTURE,
                                     'Bearer test1',
                                     'test2',
                                     404,
                                     {}
                                 ],
                                 [
                                     TASK_FIXTURE,
                                     'Bearer test2',
                                     'test1',
                                     404,
                                     {}
                                 ]
                         )
                         )
def test_retrieve_profile(test_client, retrieve_profile_fixture, token, username, expected_code,
                          expected_result):
    response = test_client.get(f'/api/v1/profiles/{username}', headers={'Authorization': token})
    assert response.status_code == expected_code
    if expected_result:
        assert response.json() == expected_result
