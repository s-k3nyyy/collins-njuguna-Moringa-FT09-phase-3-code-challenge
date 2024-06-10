
from database.connection import get_db_connection
from .author import Author
from .magazine import Magazine

class Article:
    def __init__(self, id, title, content, author_id, magazine_id):
        self._id = id
        self.title = title
        self.content = content
        self.author_id = author_id
        self.magazine_id = magazine_id

        with get_db_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO articles (title, content, author_id, magazine_id) VALUES (?, ?, ?, ?)",
                           (title, content, author_id, magazine_id))
            self._id = cursor.lastrowid
            conn.commit()

    @property
    def id(self):
        return self._id

    @property
    def author(self):
        with get_db_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM authors WHERE id = ?", (self.author_id,))
            data = cursor.fetchone()
            if data:
                return Author(*data)
            return None

    @property
    def magazine(self):
        with get_db_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM magazines WHERE id = ?", (self.magazine_id,))
            data = cursor.fetchone()
            if data:
                return Magazine(*data)
            return None

    def __repr__(self):
        return f'<Article {self.title}>'
