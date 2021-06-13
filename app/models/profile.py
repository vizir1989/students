from typing import Optional

from pydantic import HttpUrl

from .rwmodel import RWModel


class Profile(RWModel):
    username: str
    bio: Optional[str] = ""
    image: Optional[HttpUrl] = None
    following: bool = False


class ProfileInResponse(RWModel):
    profile: Profile
