import os

import pytest

dir_path = os.path.dirname(os.path.realpath(__file__))

TASK_FIXTURE = os.path.join(dir_path, 'fixture')


@pytest.mark.parametrize('fixtures_dir, expected_code, expected_result',
                         (
                                 [
                                     TASK_FIXTURE,
                                     200,
                                     {'tags': ['tag 1', 'tag 2']},
                                 ],
                         )
                         )
def test_get_tags(test_client, get_tags_fixture, expected_code,
                  expected_result):
    response = test_client.get(f'/api/v1/tags')
    assert response.status_code == expected_code
    if expected_result:
        assert response.json() == expected_result
