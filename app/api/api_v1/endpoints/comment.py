from fastapi import APIRouter, Body, Depends, Path
from starlette.status import HTTP_201_CREATED, HTTP_204_NO_CONTENT

from app.core.jwt import get_current_user_authorizer
from app.core.utils import create_aliased_response
from app.crud.comment import create_comment, get_comments_for_article, delete_comment_or_404
from app.crud.shortcuts import get_article_or_404
from app.db.mongodb.db import AsyncIOMotorClient, get_database
from app.models.comment import (
    CommentInCreate,
    CommentInResponse,
    ManyCommentsInResponse,
)
from app.models.user import User

router = APIRouter()


@router.post(
    "/articles/{slug}/comments",
    response_model=CommentInResponse,
    tags=["comments"],
    status_code=HTTP_201_CREATED,
)
async def create_comment_for_article(
        *,
        slug: str = Path(..., min_length=5),
        comment: CommentInCreate = Body(..., embed=True),
        user: User = Depends(get_current_user_authorizer()),
        db: AsyncIOMotorClient = Depends(get_database),
):
    await get_article_or_404(db, slug, user.user.username)

    dbcomment = await create_comment(db, slug, comment, user.user.username)
    return create_aliased_response(CommentInResponse(comment=dbcomment), status_code=HTTP_201_CREATED)


@router.get(
    "/articles/{slug}/comments",
    response_model=ManyCommentsInResponse,
    tags=["comments"],
)
async def get_comment_from_article(
        slug: str = Path(..., min_length=5),
        user: User = Depends(get_current_user_authorizer(required=False)),
        db: AsyncIOMotorClient = Depends(get_database),
):
    await get_article_or_404(db, slug, user.user.username)

    dbcomments = await get_comments_for_article(db, slug, user.user.username)
    return create_aliased_response(ManyCommentsInResponse(comments=dbcomments))


@router.delete(
    "/articles/{slug}/comments/{id}", tags=["comments"], status_code=HTTP_204_NO_CONTENT
)
async def delete_comment_from_article(
        slug: str = Path(..., min_length=5),
        id: str = Path(..., ge=1),
        user: User = Depends(get_current_user_authorizer()),
        db: AsyncIOMotorClient = Depends(get_database),
):
    await get_article_or_404(db, slug, user.user.username)

    await delete_comment_or_404(db, id, user.user.username)
