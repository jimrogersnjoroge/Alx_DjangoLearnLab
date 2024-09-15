Detailed configuration of views

BookListView:
    Use: Retrieves and displays a list of all books.
    Authentication:Uses TokenAuthentication
    Permissions: Configured to IsAuthenticatedOrReadOnly  ensuring
    anyone can read the list of books

BookDetailView
    Use: For retrieving a single book by ID.
    Authentication:Uses TokenAuthentication
    Permissions: Configured to IsAuthenticatedOrReadOnly  allowing both 
    Authenticated and Aunauthenticated users to view details of the book instance

BookCreateView
 Use: For adding a new book
    Authentication:Uses TokenAuthentication
    Permissions: Configured to IsAuthenticated allowing only
    Authenticated users to add a new book instance
    Customization: The perform_create method is overridden to check if a book with the same title already exists. If so, it raises a ValidationError.

BookUpdateView
for adding a new book.
 Use: For modifying an existing book
    Authentication:Uses TokenAuthentication
    Permissions: Configured to IsAuthenticated allowing only
    Authenticated users to modify an existing book
    Customization: The perform_update method is overridden to check that the title field is not empty before allowing an update.
    If the title is empty, it raises a ValidationError.

BookDeleteView:
 Use: For removing an existing book from the database
    Authentication:Uses TokenAuthentication
    Permissions: Configured to IsAuthenticated ensuring only
    Authenticated users can delete an existing book
    Customization: The perform_delete method uses default behavior provided by DestroyAPIView to delete the specified book instance 
