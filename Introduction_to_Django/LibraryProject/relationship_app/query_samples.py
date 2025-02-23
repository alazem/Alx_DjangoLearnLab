from relationship_app.models import Author, Book, Library, Librarian

# Query all books by a specific author
def books_by_author(author_name):
    author = Author.objects.get(name=author_name)
    books = author.books.all()
    for book in books:
        print(f"Title: {book.title}, Author: {author.name}")

# List all books in a library
def books_in_library(library_name):
    library = Library.objects.get(name=library_name)
    books = library.books.all()
    for book in books:
        print(f"Title: {book.title}, Library: {library.name}")

# Retrieve the librarian for a library
def librarian_for_library(library_name):
    library = Library.objects.get(name=library_name)
    librarian = library.librarian
    print(f"Librarian for {library.name}: {librarian.name}")

# Sample usage
if __name__ == "__main__":
    # Query all books by a specific author
    books_by_author('J.K. Rowling')

    # List all books in a library
    books_in_library('City Library')

    # Retrieve the librarian for a library
    librarian_for_library('City Library')
