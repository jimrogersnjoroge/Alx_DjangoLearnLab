from relationship_app.models import Author, Book, Library, Librarian

def query_books_by_author(author_name):
    author = Author.objects.get(name=author_name)
    books = Book.objects.filter(author=author)
    return books

def list_books_in_library(library_name):
    library = Library.objects.get(name=library_name)
    books = library.books.all()
    return books

def retrieve_librarian_for_library(library_name):
    library = Library.objects.get(name=library_name)
    librarian = Librarian.objects.get(library=library)
    return librarian

# Example usage:
if __name__ == "__main__":
    author_books = query_books_by_author('Author Name')
    for book in author_books:
        print(f"Book Title: {book.title}")

    library_books = list_books_in_library('Library Name')
    for book in library_books:
        print(f"Book Title: {book.title}")

    librarian = retrieve_librarian_for_library('Library Name')
    print(f"Librarian Name: {librarian.name}")
