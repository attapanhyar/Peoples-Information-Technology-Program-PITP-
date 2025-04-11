# Task 2: List Operations
# Objective: Create a program to manage a list of favorite foods. The program should allow users to add, remove, and display foods.

# Instructions:

# Start with an empty list called favorite_foods.
# Display a menu with options: 1. Add food, 2. Remove food, 3. Display foods, 4. Exit.
# Allow the user to:
# Add a new food item to the list.
# Remove a food item from the list if it exists.
# Display all items in the list.
# Repeat the menu until the user chooses to exit.

# Initialize an empty list for favorite foods
favorite_foods = []

# Loop until the user decides to exit
while True:
    # Display the menu options
    print("\nMenu:")
    print("1. Add food")
    print("2. Remove food")
    print("3. Display foods")
    print("4. Exit")

    # Get the user's choice
    choice = input("Enter your choice (1-4): ")

    # Perform actions based on the user's choice
    if choice == '1':
        # Add food
        food = input("Enter the name of the food to add: ")
        favorite_foods.append(food)
        print(f"{food} added to the list.")
    elif choice == '2':
        # Remove food
        food = input("Enter the name of the food to remove: ")
        if food in favorite_foods:
            favorite_foods.remove(food)
            print(f"{food} removed from the list.")
        else:
            print(f"{food} is not in the list.")
    elif choice == '3':
        # Display foods
        print("Favorite Foods:")
        if favorite_foods:
            for item in favorite_foods:
                print(f"- {item}")
        else:
            print("The list is empty.")
    elif choice == '4':
        # Exit
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please enter a number from 1 to 4.")
