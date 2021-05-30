# import os
#
# import pytest
#
# dir_path = os.path.dirname(os.path.realpath(__file__))
#
# TASK_FIXTURE = os.path.join(dir_path, 'fixture')
#
#
# @pytest.mark.parametrize('fixtures_dir, user, expected_code',
#                          (
#                                  [
#                                      TASK_FIXTURE,
#                                      {
#                                          'username': 'test1',
#                                          'email': 'test1@email.com',
#                                          'password': '12345678'
#                                      },
#                                      200
#                                  ],
#                                  [
#                                      TASK_FIXTURE,
#                                      {
#                                          'username': 'test2',
#                                          'email': 'test2@email.com',
#                                          'password': '12345678'
#                                      },
#                                      400
#                                  ]
#                          )
#                          )
# def test_users_login(test_client, users_login_fixture, user, expected_code):
#     response = test_client.post('/api/v1/users/login', data=user)
#     assert response.status_code == expected_code
