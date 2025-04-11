class Book:
    __slots__ = ['title','author']    
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __eq__(self, other):
        return self.title == other.title and self.author == other.author

book1 = Book("1984", "George Orwell")
book2 = Book("1984", "George Orwell")
print(book1 == book2)  # Output: True