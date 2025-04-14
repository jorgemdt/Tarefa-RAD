import sqlite3

class Book:
    def __init__(self, title: str, author: str, year: int):
        self.title = title
        self.author = author
        self.year = year

    def __str__(self):
        return f"{self.title} - {self.author} ({self.year})"

class BookModel:
    def __init__(self, db_name='books.db'):
        self.conn = sqlite3.connect(db_name)
        self.create_table()

    def create_table(self):
        with self.conn:
            self.conn.execute('''
                CREATE TABLE IF NOT EXISTS books (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    title TEXT NOT NULL,
                    author TEXT NOT NULL,
                    year INTEGER NOT NULL
                );
            ''')

    def add_book(self, book: Book):
        with self.conn:
            self.conn.execute('INSERT INTO books (title, author, year) VALUES (?, ?, ?)',
                              (book.title, book.author, book.year))

    def get_all_books(self) -> list:
        cursor = self.conn.cursor()
        cursor.execute('SELECT title, author, year FROM books')
        rows = cursor.fetchall()
        return [Book(title, author, year) for title, author, year in rows]

    def remove_book(self, index: int):
        cursor = self.conn.cursor()
        cursor.execute('SELECT id FROM books')
        ids = cursor.fetchall()
        if 0 <= index < len(ids):
            book_id = ids[index][0]
            with self.conn:
                self.conn.execute('DELETE FROM books WHERE id = ?', (book_id,))
            return True
        return False
