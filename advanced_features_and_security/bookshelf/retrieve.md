from bookshelf.models import Book

#Retrieving the books
books = Book.objects.get.all()                                 

#iterating through the records of the books
for book in books:
    print(book.title, book.author, book.publication_year)       

#Expected outcome
1984 George Orwell 1949
