import sqlite3

DB_NAME = "library.db"



def init_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()  
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS books (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            author TEXT NOT NULL,
            year INTEGER NOT NULL,
            isbn TEXT NOT NULL UNIQUE
        )
    ''')
    conn.commit()
    conn.close()

def add_book(title,author,year,isbn):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO books (title,author,year,isbn) VALUES (?,?,?,?)",(title,author,year,isbn))
    conn.commit()
    conn.close()

def view_books():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM books LIMIT 10")
    rows = cursor.fetchall()
    conn.close()
    return rows

def delete_book(book_id):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM books WHERE id=?",(book_id,))
    conn.commit()
    conn.close()


def search_by_author(author):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM books WHERE author=?",(author,))
    rows = cursor.fetchall()
    conn.close()
    return rows

def search_by_year(year):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM books WHERE year=?",(year,))
    rows = cursor.fetchall()
    conn.close()
    return rows

def update_book(book_id, title=None, author=None, year=None, isbn=None):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    fields = []
    values = []
    if title:
        fields.append("title=?")
        values.append(title)
    if author:
        fields.append("author=?")
        values.append(author)
    if year:
        fields.append("year=?")
        values.append(year)
    if isbn:
        fields.append("isbn=?")
        values.append(isbn)
    values.append(book_id)


    sql = f"UPDATE books SET {', '.join(fields)} WHERE id=?"

    cursor.execute(sql, tuple(values))
    conn.commit()
    conn.close()
    