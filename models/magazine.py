# models/magazine.py

class Magazine:
    def __init__(self, name, category):
        self._id = None
        self.name = name
        self.category = category

        from database.connection import get_db_connection
        with get_db_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO magazines (name, category) VALUES (?, ?)", (name, category))
            self._id = cursor.lastrowid
            conn.commit()

    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str) or len(value) < 2 or len(value) > 16:
            raise ValueError("Name must be a string between 2 and 16 characters.")
        self._name = value

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        if not isinstance(value, str) or len(value) == 0:
            raise ValueError("Category must be a non-empty string.")
        self._category = value

    def __repr__(self):
        return f'<Magazine {self.name}>'

    def articles(self):
        from database.connection import get_db_connection
        with get_db_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM articles WHERE magazine_id = ?", (self.id,))
            return cursor.fetchall()

    def contributors(self):
        from database.connection import get_db_connection
        with get_db_connection() as conn:
            cursor = conn.cursor()
            cursor.execute('''SELECT DISTINCT a.* FROM authors a
                              JOIN articles ar ON a.id = ar.author_id
                              WHERE ar.magazine_id = ?''', (self.id,))
            return cursor.fetchall()
