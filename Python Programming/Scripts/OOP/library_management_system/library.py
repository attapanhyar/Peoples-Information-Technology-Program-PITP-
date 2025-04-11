from book import Book
from member import Member

class Library:
    def __init__(self):
        self.books = []
        self.members = []

    def add_book(self, book):
        self.books.append(book)
        print(f'Book "{book.title}" added to the library.')

    def add_member(self, member):
        self.members.append(member)
        print(f'Member "{member.name}" added to the library.')

    def show_available_books(self):
        print("Available books:")
        for book in self.books:
            if book.is_available:
                print(book)

    def show_all_books(self):
        print("All books in the library:")
        for book in self.books:
            print(f'{book} - {"Available" if book.is_available else "Borrowed"}')

    def show_members(self):
        print("Members of the library:")
        for member in self.members:
            print(member)
