import os

from databases import DatabaseURL
from dotenv import load_dotenv
from starlette.datastructures import CommaSeparatedStrings, Secret

API_V1_STR = "/api"

load_dotenv(".env")

JWT_TOKEN_PREFIX = "Token"
ACCESS_TOKEN_EXPIRE_MINUTES = 60 * 24 * 7  # one week

MONGO_MAX_CONNECTIONS_COUNT = int(os.getenv("MONGO_MAX_CONNECTIONS_COUNT", 10))
MONGO_MIN_CONNECTIONS_COUNT = int(os.getenv("MONGO_MIN_CONNECTIONS_COUNT", 10))
SECRET_KEY = Secret(os.getenv("SECRET_KEY", "secret key for project"))

PROJECT_NAME = os.getenv("PROJECT_NAME", "FastAPI example application")
ALLOWED_HOSTS = CommaSeparatedStrings(os.getenv("ALLOWED_HOSTS", ""))

MONGODB_URL = os.getenv("MONGODB_URL", "")
MONGO_INITDB_DATABASE = os.getenv("MONGO_INITDB_DATABASE", "fastapi")

if not MONGODB_URL:
    MONGO_HOST = os.getenv("MONGO_HOST", "localhost")
    MONGO_PORT = int(os.getenv("MONGO_PORT", 27017))
    MONGO_INITDB_ROOT_USERNAME = os.getenv("MONGO_INITDB_ROOT_USERNAME", "admin")
    MONGO_INITDB_ROOT_PASSWORD = os.getenv("MONGO_INITDB_ROOT_PASSWORD", "admin")

    MONGODB_URL = DatabaseURL(
        f"mongodb://{MONGO_INITDB_ROOT_USERNAME}:{MONGO_INITDB_ROOT_PASSWORD}@{MONGO_HOST}:{MONGO_PORT}/{MONGO_INITDB_DATABASE}"
    )
else:
    MONGODB_URL = DatabaseURL(MONGODB_URL)

database_name = MONGO_INITDB_DATABASE
article_collection_name = "articles"
favorites_collection_name = "favorites"
tags_collection_name = "tags"
users_collection_name = "users"
comments_collection_name = "commentaries"
followers_collection_name = "followers"
