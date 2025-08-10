class Book:
    """A class representing a book with title, author, and publication year."""
    
    def __init__(self, title, author, year):
        """Initialize a Book instance.
        
        Args:
            title: The title of the book
            author: The author of the book  
            year: The publication year of the book
        """
        self.title = str(title)
        self.author = str(author)
        self.year = int(year)
    
    def __del__(self):
        """Destructor method called when the object is deleted."""
        try:
            print(f"Deleting {self.title}")
        except Exception:
            pass
    
    def __str__(self):
        """Return a human-readable string representation of the book.
        
        Returns:
            str: A formatted string with book details
        """
        return f"{self.title} by {self.author}, published in {self.year}"
    
    def __repr__(self):
        """Return a detailed string representation for developers.
        
        Returns:
            str: A string that can recreate the object
        """
        return f"Book('{self.title}', '{self.author}', {self.year})"