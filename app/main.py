from fastapi import FastAPI
from starlette.exceptions import HTTPException
from starlette.middleware.cors import CORSMiddleware
from starlette.status import HTTP_422_UNPROCESSABLE_ENTITY

from app.api.api_v1.api import router as api_v1_router, API_VERSION as V1
from app.core.config import ALLOWED_HOSTS, API_STR, PROJECT_NAME
from app.core.errors import http_422_error_handler, http_error_handler
from app.db.mongodb.db_utils import close_mongo_connection, connect_to_mongo

authorizations = {
    'apikey': {
        'type': 'apiKey',
        'in': 'header',
        'name': 'authorization'
    }
}

app = FastAPI(title=PROJECT_NAME, authorizations=authorizations, security='apikey',)

if not ALLOWED_HOSTS:
    ALLOWED_HOSTS = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=ALLOWED_HOSTS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.add_event_handler("startup", connect_to_mongo)
app.add_event_handler("shutdown", close_mongo_connection)

app.add_exception_handler(HTTPException, http_error_handler)
app.add_exception_handler(HTTP_422_UNPROCESSABLE_ENTITY, http_422_error_handler)

app.include_router(api_v1_router, prefix=f'{API_STR}{V1}')
