from sqlalchemy import Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import relationship
from .database import Base


book_author_table = Table(
    "books_book_authors", Base.metadata,
    Column("book_id", ForeignKey("books_book.id")),
    Column("author_id", ForeignKey("books_author.id"))
)

book_language_table = Table(
    "books_book_languages", Base.metadata,
    Column("book_id", ForeignKey("books_book.id")),
    Column("language_id", ForeignKey("books_language.id"))
)

book_subject_table = Table(
    "books_book_subjects", Base.metadata,
    Column("book_id", ForeignKey("books_book.id")),
    Column("subject_id", ForeignKey("books_subject.id"))
)

book_bookshelf_table = Table(
    "books_book_bookshelves", Base.metadata,
    Column("book_id", ForeignKey("books_book.id")),
    Column("bookshelf_id", ForeignKey("books_bookshelf.id"))
)


class Book(Base):
    __tablename__ = "books_book"
    id = Column(Integer, primary_key=True)
    gutenberg_id = Column(Integer, unique=True, nullable=False)
    title = Column(String(1024))
    download_count = Column(Integer)
    media_type = Column(String(16))

    author = relationship("Author", secondary=book_author_table, back_populates="books")
    language = relationship("Language", secondary=book_language_table, back_populates="books")
    subjects = relationship("Subject", secondary=book_subject_table, back_populates="books")
    bookshelves = relationship("Bookshelf", secondary=book_bookshelf_table, back_populates="books")
    formats = relationship("Format", back_populates="book")


class Author(Base):
    __tablename__ = "books_author"
    id = Column(Integer, primary_key=True)
    name = Column(String(128))
    birth_year = Column(Integer)
    death_year = Column(Integer)

    books = relationship("Book", secondary=book_author_table, back_populates="author")


class Format(Base):
    __tablename__ = "books_format"
    id = Column(Integer, primary_key=True)
    mime_type = Column(String(32))
    url = Column(String(256))
    book_id = Column(Integer, ForeignKey("books_book.id"))

    book = relationship("Book", back_populates="formats")


class Language(Base):
    __tablename__ = "books_language"
    id = Column(Integer, primary_key=True)
    code = Column(String(4))

    books = relationship("Book", secondary=book_language_table, back_populates="language")


class Subject(Base):
    __tablename__ = "books_subject"
    id = Column(Integer, primary_key=True)
    name = Column(String(256))

    books = relationship("Book", secondary=book_subject_table, back_populates="subjects")


class Bookshelf(Base):
    __tablename__ = "books_bookshelf"
    id = Column(Integer, primary_key=True)
    name = Column(String(64))

    books = relationship("Book", secondary=book_bookshelf_table, back_populates="bookshelves")
