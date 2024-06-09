from database.setup import create_tables
from models.article import Article
from models.author import Author
from models.magazine import Magazine

def main():
    # Initialize the database and create tables
    create_tables()

    # Collect user input
    author_name = input("Enter author's name: ")
    magazine_name = input("Enter magazine name: ")
    magazine_category = input("Enter magazine category: ")
    article_title = input("Enter article title (5-50 characters): ")
    article_content = input("Enter article content: ")

    if not (5 <= len(article_title) <= 50):
        print("Error: Article title must be between 5 and 50 characters.")
        return

    # Create an author
    author = Author(None, author_name)
    print(f"Created {author}")

    # Create a magazine
    magazine = Magazine(magazine_name, magazine_category)
    print(f"Created {magazine}")

    # Create an article
    article = Article(None, article_title, article_content, author.id, magazine.id)
    print(f"Created {article}")

    # Display results from database
    print("\nAuthors:")
    for a in author.articles():
        print(a)
    
    print("\nMagazines:")
    for m in author.magazines():
        print(m)

    print("\nMagazine Articles:")
    for ma in magazine.articles():
        print(ma)

    print("\nMagazine Contributors:")
    for mc in magazine.contributors():
        print(mc)

if __name__ == "__main__":
    main()
