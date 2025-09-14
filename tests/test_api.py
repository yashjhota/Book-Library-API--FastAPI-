import pytest
from fastapi.testclient import TestClient
from main import app
# (pytest + httpx)

client = TestClient(app)

def test_add_book():
    response = client.post("/books", json={
        "title": "1984",
        "author": "George Orwell",
        "year": 1949,
        "isbn": "1234567890123"
    })
    assert response.status_code == 200
    assert response.json()["message"] == "Book added successfully!"

def test_get_books():
    response = client.get("/books")
    assert response.status_code == 200
    assert "books" in response.json()
    