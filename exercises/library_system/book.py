class Book:
    def __init__(self, title: str, author: str, isbn: str, available: bool = True):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.available = available

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title:str):
        if isinstance(title, str) and (len(title) > 0):
            self._title = title
        else:
            raise ValueError("Title must be a string and have at least one character")

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, author:str):
        if isinstance(author, str) and (len(author) > 0):
            self._author = author
        else:
            raise ValueError("Author must be a string and have at least one character")

    @property
    def isbn(self):
        return self._isbn

    @isbn.setter
    def isbn(self, isbn:str):
        if isinstance(isbn, str) and (len(isbn) == 13):
            self._isbn = isbn
        else:
            raise ValueError("ISBN must be a string and have 13 characters")

    @property
    def available(self):
        return self._available

    @available.setter
    def available(self, available:bool):
        if isinstance(available, bool):
            self._available = available
        else:
            raise ValueError("Available must be either true or false")

    def __str__(self):
        status = "Available" if self.available else "Checked out"
        return f"{self.title} by {self.author} (ISBN: {self.isbn}) - {status}"
