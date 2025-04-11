# main.py

from book import Book
from member import Member
from library import Library

def main():
    # Create a library instance
    library = Library()

    # Add some books to the library
    book1 = Book('The Great Gatsby', 'F. Scott Fitzgerald', '123456789')
    book2 = Book('1984', 'George Orwell', '987654321')
    book3 = Book('To Kill a Mockingbird', 'Harper Lee', '555555555')

    library.add_book(book1)
    library.add_book(book2)
    library.add_book(book3)

    # Add members to the library
    member1 = Member('Alice', 'M001')
    member2 = Member('Bob', 'M002')

    library.add_member(member1)
    library.add_member(member2)

    # Show all books and members
    print("\nInitial Library State:")
    library.show_all_books()
    library.show_members()

    # Alice borrows a book
    print("\nAlice borrows '1984':")
    member1.borrow_book(book2)

    # Try borrowing the same book again
    print("\nBob tries to borrow '1984':")
    member2.borrow_book(book2)

    # Show available books
    print("\nAvailable books after borrowing:")
    library.show_available_books()

    # Alice returns the book
    print("\nAlice returns '1984':")
    member1.return_book(book2)

    # Show all books
    print("\nLibrary state after returning:")
    library.show_all_books()

if __name__ == "__main__":
    main()
