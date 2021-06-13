import os

import pytest

dir_path = os.path.dirname(os.path.realpath(__file__))

TASK_FIXTURE = os.path.join(dir_path, 'fixture')


@pytest.mark.parametrize('fixtures_dir, token, user, expected_code, expected_result',
                         (
                                 [
                                     TASK_FIXTURE,
                                     'Bearer test1',
                                     {'user': {'username': 'test3',
                                               'email': 'test3@email.com',
                                               'password': '12345678',
                                               'bio': 'bio 1',
                                               'image': 'http://fake.com/fake.jpg'}},
                                     200,
                                     {'user': {'username': 'test3', 'email': 'test3@email.com', 'bio': 'bio 1',
                                               'image': 'http://fake.com/fake.jpg'}, 'access_token': 'test1',
                                      'token_type': 'Bearer'}
                                 ],
                                 [
                                     TASK_FIXTURE,
                                     'Bearer test1',
                                     {'user': {'username': 'test2',
                                               'email': 'test3@email.com',
                                               'password': '12345678',
                                               'bio': 'bio 1',
                                               'image': 'http://fake.com/fake.jpg'}},
                                     422,
                                     {}
                                 ],
                                 [
                                     TASK_FIXTURE,
                                     'Bearer test1',
                                     {'user': {'username': 'test3',
                                               'email': 'test2@email.com',
                                               'password': '12345678',
                                               'bio': 'bio 1',
                                               'image': 'http://fake.com/fake.jpg'}},
                                     422,
                                     {}
                                 ],
                                 [
                                     TASK_FIXTURE,
                                     'Bearer test3',
                                     {'user': {'username': 'test3',
                                               'email': 'test2@email.com',
                                               'password': '12345678',
                                               'bio': 'bio 1',
                                               'image': 'http://fake.com/fake.jpg'}},
                                     404,
                                     {}
                                 ]
                         )
                         )
def test_update_user(test_client, update_user_fixture, token, user, expected_code, expected_result):
    response = test_client.put(f'/api/v1/user', headers={'Authorization': token}, json=user)
    assert response.status_code == expected_code
    if expected_result:
        assert response.json() == expected_result
