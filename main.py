from fastapi import FastAPI
from models import Book
import db
import logging


db.init_db()
app = FastAPI(title="📚 Book Library API")

# Configure logger
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[logging.FileHandler("api.log"), logging.StreamHandler()]
)

logger = logging.getLogger(__name__)

@app.middleware("http")
async def log_requests(request, call_next):
    logger.info(f"Incoming request: {request.method} {request.url}")
    response = await call_next(request)
    logger.info(f"Response status: {response.status_code}")
    return response



@app.get("/")
def read_root():
    return {"message": "Welcome to the Book Library API"}

@app.post("/books")
def create_book(book : Book):
    if not book.title or not book.author or not book.year or not book.isbn:
        return {"error": "All fields are required!"}
    db.add_book(book.title, book.author, book.year, book.isbn)
    return {"message": "Book added successfully!"}

@app.get("/books")
def get_books():
    books = db.view_books()
    if not books:
        return {"error": "No books available!"}
    return {"books": books}

@app.delete("/books/{book_id}")
def delete_book(book_id : int):
    if not isinstance(book_id, int) or book_id <= 0:
        return {"error": "Invalid book ID!"}
    if not db.view_books():
        return {"error": "No books available to delete!"}
    db.delete_book(book_id)
    return {"message": "Book deleted successfully!"}


@app.get("/books/{author}")
def get_book_by_author(author):
    books=db.search_by_author(author)
    if not books:
        return {"error":"No Author Found"}
    return {"Books":books}

@app.put("/books/{book_id}")
def update_book(book_id: int, book: Book):
    if not isinstance(book_id, int) or book_id <= 0:
        return {"error": "Invalid book ID!"}
    if not db.view_books():
        return {"error": "No books available to update!"}
    db.update_book(book_id, book.title, book.author, book.year, book.isbn)
    return {"message": "Book updated successfully!"}