import os

import pytest

from app.core.config import Collection, JWT_TOKEN_PREFIX
from tests.conftest import find_all

dir_path = os.path.dirname(os.path.realpath(__file__))

TASK_FIXTURE = os.path.join(dir_path, 'fixture')


@pytest.mark.parametrize('fixtures_dir, article, username, expected_code, expected_articles_number',
                         (
                                 [
                                     TASK_FIXTURE,
                                     {
                                         'article':
                                             {
                                                 'title': 'title 1',
                                                 'description': 'description 1',
                                                 'body': 'body 1',
                                                 'tagList': ['tag 1', 'tag 2']
                                             }
                                     },
                                     'test1',
                                     422,
                                     1
                                 ],
                                 [
                                     TASK_FIXTURE,
                                     {
                                         'article':
                                             {
                                                 'title': 'title 2',
                                                 'description': 'description 2',
                                                 'body': 'body 2',
                                                 'tagList': ['tag 1', 'tag 3']
                                             }
                                     },
                                     'test1',
                                     201,
                                     1
                                 ],
                                 [
                                     TASK_FIXTURE,
                                     {
                                         'article':
                                             {
                                                 'title': 'title 2',
                                                 'description': 'description 2',
                                                 'body': 'body 2',
                                                 'tagList': ['tag 1', 'tag 3']
                                             }
                                     },
                                     'test2',
                                     404,
                                     0
                                 ]
                         )
                         )
def test_create_new_article(test_client, create_new_article_fixture, article, username, expected_code,
                            expected_articles_number):
    token = JWT_TOKEN_PREFIX + ' ' + username
    response = test_client.post('/api/v1/articles', headers={'Authorization': token}, json=article)
    assert response.status_code == expected_code
    collection_filter = {'title': article['article']['title'], 'author_id': username}
    assert len(find_all(Collection.article.value, collection_filter)) == expected_articles_number
