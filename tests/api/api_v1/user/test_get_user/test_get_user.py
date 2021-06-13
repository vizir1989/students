import os

import pytest

dir_path = os.path.dirname(os.path.realpath(__file__))

TASK_FIXTURE = os.path.join(dir_path, 'fixture')


@pytest.mark.parametrize('fixtures_dir, token, expected_code, expected_result',
                         (
                                 [
                                     TASK_FIXTURE,
                                     'Bearer test1',
                                     200,
                                     {'username': 'test1', 'email': 'test1@email.com', 'bio': '', 'image': None}
                                 ],
                                 [
                                     TASK_FIXTURE,
                                     'Bearer test2',
                                     404,
                                     {}
                                 ]
                         )
                         )
def test_get_user(test_client, get_user_fixture, token, expected_code, expected_result):
    response = test_client.get(f'/api/v1/user', headers={'Authorization': token})
    assert response.status_code == expected_code
    if expected_result:
        assert response.json() == expected_result
