import os

import pytest

from app.core.config import article_collection_name
from tests.conftest import find_all

dir_path = os.path.dirname(os.path.realpath(__file__))

TASK_FIXTURE = os.path.join(dir_path, 'fixture')


@pytest.mark.parametrize('fixtures_dir, slug, token, expected_code, article_before, article_after',
                         (
                                 [
                                     TASK_FIXTURE,
                                     'title-1',
                                     "Bearer test1",
                                     204,
                                     1,
                                     0
                                 ],
                                 [
                                     TASK_FIXTURE,
                                     'title-2',
                                     'Bearer test1',
                                     404,
                                     0,
                                     0
                                 ],
                                 [
                                     TASK_FIXTURE,
                                     'title-1',
                                     'Bearer test2',
                                     404,
                                     1,
                                     1
                                 ]
                         )
                         )
def test_delete_article_fixture(test_client, delete_article_fixture, slug, token, expected_code, article_before,
                                article_after):
    assert len(find_all(article_collection_name, {'slug': slug})) == article_before
    response = test_client.delete(f'/api/v1/articles/{slug}', headers={'Authorization': token})
    assert response.status_code == expected_code
    assert len(find_all(article_collection_name, {'slug': slug})) == article_after
