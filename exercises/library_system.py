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
    def title(self, title):
        if isinstance(title, str) and (len(title) > 0):
            self._title = title
        else:
            raise ValueError("Title must be a string and have at least one character")

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, author):
        if isinstance(author, str) and (len(author) > 0):
            self._author = author
        else:
            raise ValueError("Author must be a string and have at least one character")

    @property
    def isbn(self):
        return self._isbn

    @isbn.setter
    def isbn(self, isbn):
        if isinstance(isbn, str) and (len(isbn) == 13):
            self._isbn = isbn
        else:
            raise ValueError("ISBN must be a string and have 13 characters")

    @property
    def available(self):
        return self._available

    @available.setter
    def available(self, available):
        if isinstance(available, bool):
            self._available = available
        else:
            raise ValueError("Available must be either true or false")

    def __str__(self):
        status = "Available" if self.available else "Checked out"
        return f"{self.title} by {self.author} (ISBN: {self.isbn}) - {status}"


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, isbn):
        self.books = [book for book in self.books if book.isbn != isbn]

    def find_book(self, isbn):
        book = [str(book) for book in self.books if book.isbn == isbn]
        if book:
            return "".join(book)
        return "Book not found"

    def display_books(self):
        if not self.books:
            return "No books available"
        books = [str(book) for book in self.books]
        return "\n".join(books)


book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", "1234567890974")
book2 = Book("1984", "George Orwell", "1234567891023")
book3 = Book("To Kill a Mockingbird", "Harper Lee", "1234567892564")

library1 = Library()

library1.add_book(book1)
library1.add_book(book2)
library1.add_book(book3)

print(library1.find_book("1234667890974"))
library1.remove_book("1234567890974")
print(library1.display_books())
