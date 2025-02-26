from relationship_app.models import Book, Author, Library, Librarian

def book_by_author(author_name):
    author = Author.objects.get(name=author_name)
    books = author.books.all()
    for books in books:
        print (f"Title:{books.title}, Author:{author.name}")

def books_in_library(library_name):
    library = Library.objects.get(name = library_name)
    books = library.books.all
    for books in books:
        print(f"Title: {books.title}, Library: {library.name}")
def librarian_for_library(library_name):
    library = Library.objects.get(name=library_name)
    librarian = library.librarians.all()
    for librarian in librarian:
        print(f"Librarian: {librarian.name}, Library: {library.name}")
        
if __name__ == '__main__':
    book_by_author('J.K. Rowling')
    books_in_library('Hogwarts')
    librarian_for_library('Hogwarts')