# : AMNA NAQI SHAIKH

# : Python Program|using if,else Statement , def Function , while loop , list ,and Exception Handling

# : LIBRARY MANAGEMENT SYSTEM

name=input("Plz Enter your name:")
num=[str(i) for i in range(10)]

print(f"Asalam u alikum,Welcome to Library Management System {name.upper()}")
print("1:Borrow book")
print("2:Return book")
print("3:Visit Library")
print("4:Study in Library")
print("5:Exit")

def Borrow_book():
    Book_title=input("\nPlz don`t enter any number in title name\nEnter the title of book you want:")
    if any(char.isdigit() for char in Book_title):
        raise ValueError("plz don`t enter number in book title.")
    print(f"{name.upper()} you have successfully borrowed:{Book_title}")
    print("you must return it within one month.")

def Return_book():
    Book_title=input("\nPlz don`t enter any number in title name\nEnter the title of book you want:")
    if any(char.isdigit() for char in Book_title):
        raise ValueError("plz don`t enter number in the book title")
    print(f"{name.upper()},you have successfully returned:{Book_title}")
    print("Thank you")
def visit_library():
            print(f"{name.upper()},I hope you like our service and management.")
            print("Thank you!")

def study_in_library():
            print(f"{name.upper()},You can study peacefully with no disturbance.")
            print("Thank you!")


flag=True
while True:
    try:
        option = int(input("Choose an option (1-5):"))
        if(option>5) or (option<1):
            raise ValueError("You entered an invalid option")
    except ValueError as e:
         print(e)
    else:
        if option == 1:
            try:
                Borrow_book()
            except ValueError as e:
                 print(e)
        elif option == 2:
            try:
                Return_book()
            except ValueError as e:
                print(e)
        elif option == 3:
            visit_library()
        elif option == 4:
            study_in_library() 
        else:
            print("Allah Hafiz!")
            break