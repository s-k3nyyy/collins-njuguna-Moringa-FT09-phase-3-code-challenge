class Article:
    def __init__(self, id, title, content, author_id, magazine_id):
        self._id = id
        self.title = title  # This will trigger the setter
        self.content = content  # This will trigger the setter
        self.author_id = author_id
        self.magazine_id = magazine_id

        from database.connection import get_db_connection
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
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        if not isinstance(value, str) or not (5 <= len(value) <= 50):
            raise ValueError("Title must be a string between 5 and 50 characters.")
        self._title = value

    @property
    def content(self):
        return self._content

    @content.setter
    def content(self, value):
        if not isinstance(value, str) or len(value) == 0:
            raise ValueError("Content must be a non-empty string.")
        self._content = value

    def __repr__(self):
        return f'<Article {self.title}>'

    @property
    def author(self):
        from database.connection import get_db_connection
        with get_db_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM authors WHERE id = ?", (self.author_id,))
            return cursor.fetchone()

    @property
    def magazine(self):
        from database.connection import get_db_connection
        with get_db_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM magazines WHERE id = ?", (self.magazine_id,))
            return cursor.fetchone()
