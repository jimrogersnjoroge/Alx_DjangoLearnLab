#importing Book models

from bookshelf.models import Book

#Creating a Book instance 

new_book = Book.objects.create(title = "1984", author = "George Orwell", publication_year = 1949)    

#Saving the added book

new_book.save()

print(new_book)

#Expected output: 

1984 by George Orwell (1949)