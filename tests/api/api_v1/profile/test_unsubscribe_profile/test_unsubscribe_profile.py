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
                                     {'profile': {'username': 'test2', 'bio': '', 'image': None, 'following': False}}
                                 ],
                                 [
                                     TASK_FIXTURE,
                                     'Bearer test2',
                                     'test1',
                                     422,
                                     {}
                                 ]
                         )
                         )
def test_unsubscribe(test_client, profile_unsubscribe_fixture, token, username, expected_code,
                     expected_result):
    response = test_client.delete(f'/api/v1/profiles/{username}/unsubscribe', headers={'Authorization': token})
    assert response.status_code == expected_code
    if expected_result:
        assert response.json() == expected_result
