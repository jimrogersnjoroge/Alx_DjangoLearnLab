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
