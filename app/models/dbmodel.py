from datetime import datetime
from typing import Optional

from bson import ObjectId
from bson.errors import InvalidId
from pydantic import BaseModel, Field


class OID(str):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        try:
            return ObjectId(str(v))
        except InvalidId:
            raise ValueError("Not a valid ObjectId")


class DateTimeModelMixin(BaseModel):
    created_at: Optional[datetime] = Field(None, alias="createdAt")
    updated_at: Optional[datetime] = Field(None, alias="updatedAt")

    class Config:
        allow_population_by_field_name = True


class DBModelMixin(DateTimeModelMixin):
    id: Optional[OID] = None
