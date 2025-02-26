from relationship_app.models import Book, Author, Library, Librarian

def book_by_author(author_name):
    author = Author.objects.filter(name=author_name).first()
    if not author:
        print(f"No author found with name: {author_name}")
        return

    books = author.books.all()
    for book in books:  # Use singular 'book'
        print(f"Title: {book.title} by Author: {author.name}")

def books_in_library(library_name):
    library = Library.objects.filter(name=library_name).first()
    if not library:
        print(f"No library found with name: {library_name}")
        return

    books = library.books.all()  # Corrected missing parentheses
    for book in books:  # Use singular 'book'
        print(f"Title: {book.title}, Library: {library.name}")

def librarian_for_library(library_name):
    library = Library.objects.filter(name=library_name).first()
    if not library:
        print(f"No library found with name: {library_name}")
        return

    librarians = library.librarians.all()
    for librarian in librarians:  # Use plural 'librarians' for clarity
        print(f"Librarian: {librarian.name}, Library: {library.name}")

if __name__ == '__main__':
    book_by_author('J.K. Rowling')
    books_in_library('Hogwarts')
    librarian_for_library('Hogwarts')
