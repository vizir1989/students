import os

import pytest

from app.core.config import users_collection_name
from tests.conftest import find_all

dir_path = os.path.dirname(os.path.realpath(__file__))

TASK_FIXTURE = os.path.join(dir_path, 'fixture')


@pytest.mark.parametrize('fixtures_dir, user, expected_code, user_number',
                         (
                                 [
                                     TASK_FIXTURE,
                                     {
                                         'username': 'test1',
                                         'email': 'test1@email.com',
                                         'password': '12345678'
                                     },
                                     200,
                                     1
                                 ],
                                 [
                                     TASK_FIXTURE,
                                     {
                                         'username': 'test2',
                                         'email': 'test2@email.com',
                                         'password': '12345678'
                                     },
                                     400,
                                     0
                                 ]
                         )
                         )
def test_users_login(test_client, users_login_fixture, user, expected_code, user_number):
    response = test_client.post('/api/v1/users/login', data=user)
    assert response.status_code == expected_code
    assert len(find_all(users_collection_name, {'username': user['username']})) == user_number
