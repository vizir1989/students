# import os
#
# import pytest
#
# from tests.conftest import FAKE_TIME
#
# dir_path = os.path.dirname(os.path.realpath(__file__))
#
# TASK_FIXTURE = os.path.join(dir_path, 'fixture')
#
#
# @pytest.mark.parametrize('fixtures_dir, token, slug, id_, expected_code, expected_result',
#                          (
#                                  [
#                                      TASK_FIXTURE,
#                                      'Bearer test1',
#                                      'title-1',
#                                      '111111111111111111111111',
#                                      200,
#                                      {"article": {"title": "title 2", "description": "description 2", "body": "body 2",
#                                                   "tagList": ["tag 1", "tag 3"], "createdAt": FAKE_TIME,
#                                                   "updatedAt": None, "slug": "title-2",
#                                                   "author": {"username": "test2", "bio": "", "image": None,
#                                                              "following": False}, "favorited": False,
#                                                   "favoritesCount": 0, "id": None}},
#                                  ],
#                                  [
#                                      TASK_FIXTURE,
#                                      'Bearer test2',
#                                      'title-1',
#                                      '111111111111111111111111',
#                                      200,
#                                      {"article": {"title": "title 1", "description": "description 1", "body": "body 1",
#                                                   "tagList": ["tag 1", "tag 2"], "createdAt": FAKE_TIME,
#                                                   "updatedAt": None, "slug": "title-1",
#                                                   "author": {"username": "test1", "bio": "", "image": None,
#                                                              "following": False}, "favorited": False,
#                                                   "favoritesCount": 0, "id": None}},
#                                  ],
#                                  [
#                                      TASK_FIXTURE,
#                                      'Bearer test1',
#                                      'title-2',
#                                      '111111111111111111111111',
#                                      404,
#                                      {},
#                                  ],
#                                  [
#                                      TASK_FIXTURE,
#                                      'Bearer test1',
#                                      'title-1',
#                                      '111111111111111111111112',
#                                      400,
#                                      {},
#                                  ]
#                          )
#                          )
# def test_delete_comment(test_client, delete_comment_fixture, token, slug, id_, expected_code, expected_result):
#     resposne = test_client.delete(f'/api/v1/articles/{slug}/comments/{id_}', headers={'Authorization': token})
#     assert resposne.status_code == expected_code
#     if expected_result:
#         assert resposne.json() == expected_result
