import unittest
from models.author import Author
from models.article import Article
from models.magazine import Magazine

class TestModels(unittest.TestCase):
    def test_author_creation(self):
        author = Author(None, "John Doe")
        self.assertEqual(author.name, "John Doe")

    def test_article_creation(self):
        article = Article(None, "Test Title", "Test Content", 1, 1)
        self.assertEqual(article.title, "Test Title")

    def test_magazine_creation(self):
        magazine = Magazine("Tech Weekly", "Technology")
        self.assertEqual(magazine.name, "Tech Weekly")
        self.assertEqual(magazine.category, "Technology")

    def test_author_repr(self):
        author = Author(None, "John Doe")
        self.assertEqual(repr(author), "<Author John Doe>")

    def test_article_repr(self):
        article = Article(None, "Test Title", "Test Content", 1, 1)
        self.assertEqual(repr(article), "<Article Test Title>")

    def test_magazine_repr(self):
        magazine = Magazine("Tech Weekly", "Technology")
        self.assertEqual(repr(magazine), "<Magazine Tech Weekly>")
    
    def test_author_articles(self):
        author = Author(None, "John Doe")
        self.assertEqual(len(author.articles()), 0)

    def test_author_magazines(self):
        author = Author(None, "John Doe")
        self.assertEqual(len(author.magazines()), 0)

    def test_magazine_articles(self):
        magazine = Magazine("Tech Weekly", "Technology")
        self.assertEqual(len(magazine.articles()), 0)

    def test_magazine_contributors(self):
        magazine = Magazine("Tech Weekly", "Technology")
        self.assertEqual(len(magazine.contributors()), 0)

if __name__ == '__main__':
    unittest.main()
