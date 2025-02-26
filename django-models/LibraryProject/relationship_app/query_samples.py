from relationship_app.models import Book, Author, Library, Librarian

def book_by_author(author_name):
    author = Author.objects.get(name=author_name)
    books = Book.objects.filter(author=author)  # Changed to use .filter()
    for book in books:
        print(f"Title: {book.title} by Author: {author.name}")

def books_in_library(library_name):
    library = Library.objects.get(name=library_name)
    books = library.books.all()
    for book in books:
        print(f"Title: {book.title}, Library: {library.name}")

def librarian_for_library(library_name):
    library = Library.objects.get(name=library_name)
    librarian = Librarian.objects.filter(library=library)  # Using filter() for retrieval
    for person in librarian:
        print(f"Librarian: {person.name}, Library: {library.name}")

if __name__ == '__main__':
    book_by_author('J.K. Rowling')
    books_in_library('Hogwarts')
    librarian_for_library('Hogwarts')
