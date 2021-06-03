import os

import pytest

from app.core.config import Collection
from tests.conftest import find_all

dir_path = os.path.dirname(os.path.realpath(__file__))

TASK_FIXTURE = os.path.join(dir_path, 'fixture')


@pytest.mark.parametrize('fixtures_dir, token, slug, expected_code, article_before, article_after',
                         (
                                 [
                                     TASK_FIXTURE,
                                     'Bearer test1',
                                     'title-1',
                                     204,
                                     1,
                                     0
                                 ],
                                 [
                                     TASK_FIXTURE,
                                     'Bearer test1',
                                     'title-2',
                                     404,
                                     0,
                                     0
                                 ],
                                 [
                                     TASK_FIXTURE,
                                     'Bearer test2',
                                     'title-1',
                                     404,
                                     1,
                                     1
                                 ]
                         )
                         )
def test_delete_article(test_client, delete_article_fixture, token, slug, expected_code, article_before,
                        article_after):
    assert len(find_all(Collection.article.value, {'slug': slug})) == article_before
    response = test_client.delete(f'/api/v1/articles/{slug}', headers={'Authorization': token})
    assert response.status_code == expected_code
    assert len(find_all(Collection.article.value, {'slug': slug})) == article_after
