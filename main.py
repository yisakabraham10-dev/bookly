from fastapi import FastAPI
from typing import Optional, List
from pydantic import BaseModel

app = FastAPI()

Books = [
    {
        "book_id": 1,
        "author": "George Orwell",
        "title": "1984",
        "publisher": "Secker & Warburg",
        "published_date": "1949-06-08",
        "page_count": 328,
        "language": "English"
    },
    {
        "book_id": 2,
        "author": "Harper Lee",
        "title": "To Kill a Mockingbird",
        "publisher": "J.B. Lippincott & Co.",
        "published_date": "1960-07-11",
        "page_count": 281,
        "language": "English"
    },
    {
        "book_id": 3,
        "author": "Paulo Coelho",
        "title": "The Alchemist",
        "publisher": "HarperTorch",
        "published_date": "1988-01-01",
        "page_count": 208,
        "language": "Portuguese"
    }
]

class Book(BaseModel):
    book_id: str
    title: str
    publisher: str
    published_date: str
    page_count: int
    language: str

@app.get("/get_books")
async def get_all_books()->dict :
    return Books
