from book import Book

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