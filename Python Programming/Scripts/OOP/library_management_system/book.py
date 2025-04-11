class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_available = True

    def __str__(self):
        return f'{self.title} by {self.author} (ISBN: {self.isbn})'

    def borrow(self):
        if self.is_available:
            self.is_available = False
            print(f'You have borrowed "{self.title}".')
        else:
            print(f'Sorry, "{self.title}" is already borrowed.')

    def return_book(self):
        self.is_available = True
        print(f'Thank you for returning "{self.title}".')
