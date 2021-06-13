import os

import pytest
from slugify import slugify

from app.core.config import Collection
from tests.conftest import find_all

dir_path = os.path.dirname(os.path.realpath(__file__))

TASK_FIXTURE = os.path.join(dir_path, 'fixture')


@pytest.mark.parametrize('fixtures_dir, token, article, expected_code, check_article',
                         (
                                 [
                                     TASK_FIXTURE,
                                     'Bearer test1',
                                     {
                                         'article':
                                             {
                                                 'title': 'title 1',
                                                 'description': 'description 2',
                                                 'body': 'body 2',
                                                 'tag_list': ['tag 1', 'tag 3']
                                             }
                                     },
                                     200,
                                     True
                                 ],
                                 [
                                     TASK_FIXTURE,
                                     'Bearer test2',
                                     {
                                         'article':
                                             {
                                                 'title': 'title 1',
                                                 'description': 'description 2',
                                                 'body': 'body 2',
                                                 'tag_list': ['tag 1', 'tag 3']
                                             }
                                     },
                                     404,
                                     False
                                 ]
                         )
                         )
def test_update_article(test_client, update_article_fixture, token, article, expected_code, check_article):
    slug = slugify(article['article']['title'])
    response = test_client.put(f'/api/v1/articles/{slug}', headers={'Authorization': token}, json=article)
    assert response.status_code == expected_code
    if check_article:
        result = find_all(Collection.article.value, {'title': article['article']['title']})
        assert len(result) == 1
        for k, v in article['article'].items():
            assert result[0][k] == v
