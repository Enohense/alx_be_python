class Book:
    """Represents a single book in the library."""

    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False

    def check_out(self):
        """Marks the book as checked out."""
        self._is_checked_out = True

    def return_book(self):
        """Marks the book as available (not checked out)."""
        self._is_checked_out = False

    def is_available(self):
        """Returns True if the book is available for checkout."""
        return not self._is_checked_out

    def __str__(self):
        return f"{self.title} by {self.author}"


class Library:
    """Manages a collection of books."""

    def __init__(self):
        self._books = []

    def add_book(self, book):
        """Adds a book to the library collection."""
        self._books.append(book)

    def check_out_book(self, title):
        """Checks out the book with the given title."""
        for book in self._books:
            if book.title == title and book.is_available():
                book.check_out()
                return
        print(f"Book '{title}' is not available for checkout.")

    def return_book(self, title):
        """Returns the book with the given title."""
        for book in self._books:
            if book.title == title and not book.is_available():
                book.return_book()
                return
        print(f"Book '{title}' was not checked out.")

    def list_available_books(self):
        """Prints all books that are available for checkout."""
        available_books = [book for book in self._books if book.is_available()]
        for book in available_books:
            print(book)
