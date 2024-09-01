#CREATING Book Instance
#importing Book models

from bookshelf.models import Book

#Creating a Book instance 

new_book = Book.objects.create(title = "1984", author = "George Orwell", publication_year = 1949)    

#Saving the added book

new_book.save()

print(new_book)

#Expected output: 

1984 by George Orwell (1949)


#RETRIEVING of the book
from bookshelf.models import Book

#Retrieving the books
books = Book.objects.get.all()                                 

#iterating through the records of the books
for book in books:
    print(book.title, book.author, book.publication_year)       

#Expected outcome
1984 George Orwell 1949


#UPDATING Book instance
from bookshelf.models import Book

book =Book.objects.get(title="1984")

#Updating the book title
book.title = Book.objects.update(title = "Nineteen Eighty-Four") 

#Saving the update
book.save()

#fetching the updated book to confirm if it was successful
updated_book = Book.objects.get(title=book.title)

#Printing the updated_book
print(updated_book)

#Output
Nineteen Eighty-Four by George Orwell (1949)


#DELETING the Book instance
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