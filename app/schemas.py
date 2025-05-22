from pydantic import BaseModel
from typing import List, Optional


class AuthorOut(BaseModel):
    id: int
    name: str
    birth_year: Optional[int]
    death_year: Optional[int]

    class Config:
        from_attributes = True


class LanguageOut(BaseModel):
    id: int
    code: str

    class Config:
        from_attributes = True


class SubjectOut(BaseModel):
    id: int
    name: str

    class Config:
        from_attributes = True


class BookshelfOut(BaseModel):
    id: int
    name: str

    class Config:
        from_attributes = True


class FormatOut(BaseModel):
    id: int
    mime_type: str
    url: str

    class Config:
        from_attributes = True


class BookOut(BaseModel):
    id: int
    gutenberg_id: int
    title: Optional[str]
    media_type: str
    download_count: Optional[int]
    author: List[AuthorOut]
    language: List[LanguageOut]
    subjects: List[SubjectOut]
    bookshelves: List[BookshelfOut]
    formats: List[FormatOut]

    class Config:
        orm_mode = True


class BookListResponse(BaseModel):
    total: int
    page: int
    page_size: int
    next_page: Optional[str] = None
    previous_page: Optional[str] = None
    books: List[BookOut]
