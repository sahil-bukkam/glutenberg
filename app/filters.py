from sqlalchemy.orm import Query
from sqlalchemy.sql import or_
from .models import Book, Language, Format, Subject, Bookshelf, Author


def apply_book_id_filter(query: Query, book_id: str):
    if book_id:
        book_ids = [int(bid.strip()) for bid in book_id.split(",") if bid.strip().isdigit()]
        if book_ids:
            query = query.filter(Book.gutenberg_id.in_(book_ids))
    return query


def apply_language_filter(query: Query, language: str):
    if language:
        languages = [lang.strip() for lang in language.split(",") if lang.strip()]
        if languages:
            query = query.filter(Book.language.any(Language.code.in_(languages)))
    return query


def apply_mime_type_filter(query: Query, mime_type: str):
    if mime_type:
        mime_types = [mt.strip() for mt in mime_type.split(",") if mt.strip()]
        if mime_types:
            query = query.filter(Book.formats.any(Format.mime_type.in_(mime_types)))
    return query


def apply_topic_filter(query: Query, topic: str):
    if topic:
        topics = [t.strip().lower() for t in topic.split(",") if t.strip()]
        topic_conditions = []
        for t in topics:
            pattern = f"%{t}%"
            topic_conditions.append(Book.subjects.any(Subject.name.ilike(pattern)))
            topic_conditions.append(Book.bookshelves.any(Bookshelf.name.ilike(pattern)))
        if topic_conditions:
            query = query.filter(or_(*topic_conditions))
    return query


def apply_author_filter(query: Query, author: str):
    if author:
        authors = [a.strip() for a in author.split(",") if a.strip()]
        author_conditions = [Book.author.any(Author.name.ilike(f"%{a}%")) for a in authors]
        if author_conditions:
            query = query.filter(or_(*author_conditions))
    return query


def apply_title_filter(query: Query, title: str):
    if title:
        titles = [t.strip() for t in title.split(",") if t.strip()]
        title_conditions = [Book.title.ilike(f"%{t}%") for t in titles]
        if title_conditions:
            query = query.filter(or_(*title_conditions))
    return query
