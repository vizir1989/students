from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel
from starlette.responses import JSONResponse
from starlette.status import HTTP_200_OK


def create_aliased_response(model: BaseModel, status_code: int = HTTP_200_OK) -> JSONResponse:
    return JSONResponse(content=jsonable_encoder(model, by_alias=True), status_code=status_code)
