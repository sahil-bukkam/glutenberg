from fastapi import APIRouter, Depends, Query, Request
from sqlalchemy.orm import Session
from ..database import SessionLocal
from ..models import Book
from ..schemas import BookListResponse
from ..filters import (
    apply_book_id_filter, apply_language_filter, apply_mime_type_filter,
    apply_topic_filter, apply_author_filter, apply_title_filter,
)
from ..pagination import build_page_url

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/api/books/", response_model=BookListResponse)
def get_books(
    request: Request,
    page: int = Query(1, ge=1),
    page_size: int = Query(25, ge=1, le=100),
    book_id: str = Query(None),
    language: str = Query(None),
    mime_type: str = Query(None),
    topic: str = Query(None),
    author: str = Query(None),
    title: str = Query(None),
    db: Session = Depends(get_db),
):
    query = db.query(Book).order_by(Book.download_count.desc())

    query = apply_book_id_filter(query, book_id)
    query = apply_language_filter(query, language)
    query = apply_mime_type_filter(query, mime_type)
    query = apply_topic_filter(query, topic)
    query = apply_author_filter(query, author)
    query = apply_title_filter(query, title)

    offset = (page - 1) * page_size
    total = query.count()
    books = query.offset(offset).limit(page_size).all()
    next_page = build_page_url(request, page + 1) if offset + page_size < total else None
    previous_page = build_page_url(request, page - 1) if page > 1 else None

    return {
        "total": total,
        "page": page,
        "page_size": page_size,
        "next_page": next_page,
        "previous_page": previous_page,
        "books": books,
    }
