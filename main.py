from fastapi import FastAPI, status
from fastapi.exceptions import HTTPException
from typing import List
from src.books.book_data import books
from src.books.schemas import Book, UpdateBook

app = FastAPI()
