# 📚 Book Library API

A simple **Book Library API** built with **FastAPI**.  
This project is part of my Python + Software Engineering learning journey, focusing on **APIs, databases, logging, testing, and CI/CD**.

---

## 🚀 Features
- Add a new book (title, author, year, ISBN)  
- Get all books  
- Search books by author (`GET /books?author=...`)  
- Update a book by ID  
- Delete a book by ID  
- Built-in API documentation via Swagger UI  

---

## 🛠️ Tech Stack
- **Python 3.10+**  
- **FastAPI** – high-performance API framework  
- **SQLite** – lightweight relational database  
- **SQLAlchemy** – ORM for database handling  
- **Pydantic** – data validation  
- **Logging** – tracks API calls & errors  
- **pytest** – for testing  
- **GitHub Actions** – CI pipeline for auto linting & tests  

---

## 📂 Project Structure
-book_library_api/
```
-   ├── main.py # FastAPI entrypoint
-   ├── models.py # Database models
-   ├── db.py # DB connection & session
-   ├── tests/ # pytest test cases
-   ├── requirements.txt
-   ├── README.md
```

---

## ⚡ Getting Started

### 1️⃣ Clone the repo
```bash
git clone https://github.com/yashjhota/book-library-api
cd book-library-api
