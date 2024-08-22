from relationship_app.models import Author, Book, Library, Librarian

#Query all books by a specific author.
author_name = "author.name"
author = Author.objects.get(name=author_name)
books = Book.objects.filter(author=author)
print(f"Books: by {author.name}")
for book in books:
    print(f" -{book.title}")


#List all books in a library.
library_name = "library.name"
library = Library.objects.get(name=library_name)
books = library.books.all()
print(f"Books in {library.name}: ")
for book in books:
    print(f" -{book.title}").objects.all()


#Retrieve the librarian for a library
librarian_name = "librarian.name"
librarian = Librarian.objects.get(library=librarian_name)
library = librarian.library
for librarian in library:
    print(f"Librarian: {librarian.name}) for ({library.name})")