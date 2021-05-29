import os

import pytest

dir_path = os.path.dirname(os.path.realpath(__file__))

TASK_FIXTURE = os.path.join(dir_path, 'fixture')


@pytest.mark.parametrize('fixtures_dir, user, expected_code',
                         (
                                 [
                                     TASK_FIXTURE,
                                     {
                                         'user':
                                             {
                                                 'username': 'test1',
                                                 'email': 'test1@email.com',
                                                 'password': '12345678'
                                             }
                                     },
                                     422
                                 ],
                                 [
                                     TASK_FIXTURE,
                                     {
                                         'user':
                                             {
                                                 'username': 'test2',
                                                 'email': 'test2@email.com',
                                                 'password': '12345678'
                                             }
                                     },
                                     201
                                 ]
                         )
                         )
def test_create_user(test_client, create_user_fixture, user, expected_code):
    response = test_client.post('/api/v1/users', json=user)
    assert response.status_code == expected_code
