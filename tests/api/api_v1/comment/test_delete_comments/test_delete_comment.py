import os

import pytest

dir_path = os.path.dirname(os.path.realpath(__file__))

TASK_FIXTURE = os.path.join(dir_path, 'fixture')


@pytest.mark.parametrize('fixtures_dir, token, slug, id_, expected_code, expected_result',
                         (
                                 [
                                     TASK_FIXTURE,
                                     'Bearer test1',
                                     'title-1',
                                     '111111111111111111111111',
                                     204,
                                     {},
                                 ],
                                 [
                                     TASK_FIXTURE,
                                     'Bearer test2',
                                     'title-1',
                                     '111111111111111111111111',
                                     404,
                                     {},
                                 ],
                                 [
                                     TASK_FIXTURE,
                                     'Bearer test1',
                                     'title-1',
                                     '111111111111111111111112',
                                     404,
                                     {},
                                 ]
                         )
                         )
def test_delete_comment(test_client, delete_comment_fixture, token, slug, id_, expected_code, expected_result):
    resposne = test_client.delete(f'/api/v1/articles/{slug}/comments/{id_}', headers={'Authorization': token})
    assert resposne.status_code == expected_code
    if expected_result:
        assert resposne.json() == expected_result
