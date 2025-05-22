from fastapi import FastAPI
from .database import Base, engine
from .routers import books

app = FastAPI(title="Gutenberg API")

Base.metadata.create_all(bind=engine)

app.include_router(books.router)
