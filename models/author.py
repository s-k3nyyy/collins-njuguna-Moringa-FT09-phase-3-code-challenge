class Author:
    def __init__(self, id, name):
        self._id = id
        self.name = name 
        self._insert_author_into_db()

    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str) or len(value) == 0:
            raise ValueError("Name must be a non-empty string.")
        self._name = value

    def __repr__(self):
        return f'<Author {self.name}>'

    def articles(self):
        from database.connection import get_db_connection
        with get_db_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM articles WHERE author_id = ?", (self.id,))
            return cursor.fetchall()

    def magazines(self):
        from database.connection import get_db_connection
        with get_db_connection() as conn:
            cursor = conn.cursor()
            cursor.execute('''SELECT DISTINCT m.* FROM magazines m
                              JOIN articles ar ON m.id = ar.magazine_id
                              WHERE ar.author_id = ?''', (self.id,))
            return cursor.fetchall()

    @classmethod
    def all(cls):
        # Retrieve all authors from the database
        from database.connection import get_db_connection
        with get_db_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM authors")
            return [cls(*row) for row in cursor.fetchall()]

    def _insert_author_into_db(self):
        from database.connection import get_db_connection
        with get_db_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("INSERT OR IGNORE INTO authors (name) VALUES (?)", (self.name,))
            if cursor.lastrowid:
                self._id = cursor.lastrowid
                conn.commit()
