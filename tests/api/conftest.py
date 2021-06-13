from pytest import fixture


@fixture(scope='function')
def create_user_fixture(mongo_load_fixture):
    pass


@fixture(scope='function')
def users_login_fixture(mongo_load_fixture, patch_verify_password):
    pass


@fixture(scope='function')
def create_new_article_fixture(mongo_load_fixture, patch_jwt_decode):
    pass


@fixture(scope='function')
def delete_article_fixture(mongo_load_fixture, patch_jwt_decode, generation_time_mock):
    pass


@fixture(scope='function')
def update_article_fixture(mongo_load_fixture, patch_jwt_decode):
    pass


@fixture(scope='function')
def get_article_fixture(mongo_load_fixture, patch_jwt_decode, generation_time_mock):
    pass


@fixture(scope='function')
def get_articles_fixture(mongo_load_fixture, patch_jwt_decode, generation_time_mock):
    pass


@fixture(scope='function')
def post_favorite_article_fixture(mongo_load_fixture, patch_jwt_decode, generation_time_mock):
    pass


@fixture(scope='function')
def delete_favorite_article_fixture(mongo_load_fixture, patch_jwt_decode, generation_time_mock):
    pass


@fixture(scope='function')
def get_comments_fixture(mongo_load_fixture, patch_jwt_decode, generation_time_mock):
    pass


@fixture(scope='function')
def create_comments_fixture(mongo_load_fixture, patch_jwt_decode, generation_time_mock):
    pass


@fixture(scope='function')
def get_article_feed_fixture(mongo_load_fixture, patch_jwt_decode, generation_time_mock):
    pass


@fixture(scope='function')
def delete_comment_fixture(mongo_load_fixture, patch_jwt_decode):
    pass


@fixture(scope='function')
def retrieve_profile_fixture(mongo_load_fixture, patch_jwt_decode):
    pass


@fixture(scope='function')
def profile_subscribe_fixture(mongo_load_fixture, patch_jwt_decode):
    pass


@fixture(scope='function')
def profile_unsubscribe_fixture(mongo_load_fixture, patch_jwt_decode):
    pass


@fixture(scope='function')
def get_tags_fixture(mongo_load_fixture, patch_jwt_decode):
    pass


@fixture(scope='function')
def get_user_fixture(mongo_load_fixture, patch_jwt_decode):
    pass


@fixture(scope='function')
def update_user_fixture(mongo_load_fixture, patch_jwt_decode):
    pass
