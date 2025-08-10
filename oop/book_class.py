class Book:
    def __init__(self, title: str, author: str, year: int) -> None:
        self.title = str(title)
        self.author = str(author)
        self.year = int(year)

    def __str__(self) -> str:
        return f"{self.title} by {self.author}, published in {self.year}"

    def __repr__(self) -> str:
        return f"Book('{self.title}', '{self.author}', {self.year})"

    def __del__(self) -> None:
        # Guard against odd shutdown states
        try:
            print(f"Deleting {self.title}")
        except Exception:
            pass

