from typing import List, Optional

from pydantic import Field

from .dbmodel import DateTimeModelMixin, DBModelMixin
from .profile import Profile
from .rwmodel import RWModel


class ArticleFilterParams(RWModel):
    tag: str = ""
    author: str = ""
    favorited: str = ""
    limit: int = 20
    offset: int = 0


class ArticleBase(RWModel):
    title: str
    description: str
    body: str
    tag_list: List[str] = Field([], alias="tagList")


class Article(DateTimeModelMixin, ArticleBase):
    slug: str
    author: Profile
    favorited: bool
    favorites_count: int = Field(..., alias="favoritesCount")


class ArticleInDB(DBModelMixin, Article):
    pass


class ArticleInResponse(RWModel):
    article: Article


class ManyArticlesInResponse(RWModel):
    articles: List[Article]
    articles_count: int = Field(0, alias="articlesCount")

    class Config:
        allow_population_by_field_name = True


class ArticleInCreate(ArticleBase):
    pass


class ArticleInUpdate(RWModel):
    title: Optional[str] = None
    description: Optional[str] = None
    body: Optional[str] = None
    tag_list: List[str] = Field([], alias="tagList")

    class Config:
        allow_population_by_field_name = True
