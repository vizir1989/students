import os

from databases import DatabaseURL
from dotenv import load_dotenv
from enum import Enum
from starlette.datastructures import CommaSeparatedStrings, Secret

API_STR = "/api"

load_dotenv(".env")

JWT_TOKEN_PREFIX = "Bearer"
ACCESS_TOKEN_EXPIRE_MINUTES = 30  # one week
SECRET_KEY = Secret(os.getenv("SECRET_KEY", "secret key for project"))
ALGORITHM = os.getenv("ALGORITHM", "HS256")

MONGO_MAX_CONNECTIONS_COUNT = int(os.getenv("MONGO_MAX_CONNECTIONS_COUNT", 10))
MONGO_MIN_CONNECTIONS_COUNT = int(os.getenv("MONGO_MIN_CONNECTIONS_COUNT", 10))


PROJECT_NAME = os.getenv("PROJECT_NAME", "FastAPI example application")
ALLOWED_HOSTS = CommaSeparatedStrings(os.getenv("ALLOWED_HOSTS", ""))

MONGODB_URL = os.getenv("MONGODB_URL", "")
MONGO_INITDB_DATABASE = os.getenv("MONGO_INITDB_DATABASE", "fastapi")

if not MONGODB_URL:
    MONGO_HOST = os.getenv("MONGO_HOST", "localhost")
    MONGO_PORT = int(os.getenv("MONGO_PORT", 27017))
    MONGO_INITDB_USERNAME = os.getenv("MONGO_INITDB_USER", "mongodb")
    MONGO_INITDB_PWD = os.getenv("MONGO_INITDB_PWD", "mongodb")

    MONGODB_URL = DatabaseURL(
        f"mongodb://{MONGO_INITDB_USERNAME}:{MONGO_INITDB_PWD}@{MONGO_HOST}:{MONGO_PORT}/{MONGO_INITDB_DATABASE}"
    )
else:
    MONGODB_URL = DatabaseURL(MONGODB_URL)

database_name = MONGO_INITDB_DATABASE


class Collection(Enum):
    article = "articles"
    favorites = "favorites"
    tags = "tags"
    users = "users"
    comments = "commentaries"
    followers = "followers"
