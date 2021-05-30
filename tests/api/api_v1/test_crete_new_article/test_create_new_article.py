import os

import pytest

from app.core.config import database_name, article_collection_name
from app.db.mongodb.db import get_database
from tests.conftest import find_all

dir_path = os.path.dirname(os.path.realpath(__file__))

TASK_FIXTURE = os.path.join(dir_path, 'fixture')


@pytest.mark.parametrize('fixtures_dir, article, token, expected_code',
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
                                     "Bearer test1",
                                     422
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
                                     'Bearer test1',
                                     201
                                 ]
                         )
                         )
def test_create_new_article(test_client, create_new_article_fixture, article, token, expected_code):
    response = test_client.post('/api/v1/articles', headers={'Authorization': token}, json=article)
    assert response.status_code == expected_code
    assert len(find_all(article_collection_name, {'title': article['article']['title']})) == 1
