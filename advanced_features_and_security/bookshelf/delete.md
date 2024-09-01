#importing Book models
from bookshelf.models import Book

#retriveing the book
book = Book.objects.get(author="George Orwell")

#Deleting the book instnace
book.delete()

#results
(1, {'bookshelf.Book': 1})

#Trying to retrieve all the books and confirm if deletion was #successful
books = Book.objects.get.all()
print(books)
#Output showing an empty list
<QuerySet []>