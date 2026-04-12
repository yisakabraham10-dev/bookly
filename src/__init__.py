from fastapi import FastAPI
from src.books.routes import book_router

version = "v1"
app = FastAPI(version = version, 
              title = "bookly", 
              description= "A backend web service for books that is built through REST API's.")

app.include_router(book_router, prefix= f"/api/{version}/book", tags= ["books,"])