
from database.connection import get_db_connection

class Author:
    def __init__(self, id, name):
        self._id = id
        self.name = name
        self._insert_author_into_db()

    @property
    def id(self):
        return self._id

    def articles(self):
        with get_db_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM articles WHERE author_id = ?", (self.id,))
            data = cursor.fetchall()
            return [Article(*row) for row in data]

    def magazines(self):
        with get_db_connection() as conn:
            cursor = conn.cursor()
            cursor.execute('''SELECT DISTINCT m.* FROM magazines m
                              JOIN articles ar ON m.id = ar.magazine_id
                              WHERE ar.author_id = ?''', (self.id,))
            data = cursor.fetchall()
            return [Magazine(*row) for row in data]

    @classmethod
    def all(cls):
        with get_db_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM authors")
            return [cls(*row) for row in cursor.fetchall()]

    def _insert_author_into_db(self):
        with get_db_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("INSERT OR IGNORE INTO authors (name) VALUES (?)", (self.name,))
            if cursor.lastrowid:
                self._id = cursor.lastrowid
                conn.commit()

    def __repr__(self):
        return f'<Author {self.name}>'
