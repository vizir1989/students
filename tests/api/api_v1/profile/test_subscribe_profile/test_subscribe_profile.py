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
                                     422,
                                     {}
                                 ],
                                 [
                                     TASK_FIXTURE,
                                     'Bearer test1',
                                     'test2',
                                     200,
                                     {'profile': {'username': 'test2', 'bio': '', 'image': None, 'following': True}}
                                 ],
                                 [
                                     TASK_FIXTURE,
                                     'Bearer test2',
                                     'test3',
                                     422,
                                     {}
                                 ],
                                 [
                                     TASK_FIXTURE,
                                     'Bearer test3',
                                     'test4',
                                     404,
                                     {}
                                 ]
                         )
                         )
def test_profile_subscribe(test_client, profile_subscribe_fixture, token, username, expected_code,
                           expected_result):
    response = test_client.post(f'/api/v1/profiles/{username}/subscribe', headers={'Authorization': token})
    assert response.status_code == expected_code
    if expected_result:
        assert response.json() == expected_result
