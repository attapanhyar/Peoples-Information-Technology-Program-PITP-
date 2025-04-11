# Initialize a starting balance
balance = 0.0

# Function to display the main menu
def show_menu():
    print("\n--- Banking System ---")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Exit")

# Function to deposit money
def deposit():
    global balance
    try:
        # Get deposit amount from the user
        amount = float(input("Enter amount to deposit: "))
        
        if amount <= 0:
            raise ValueError("Deposit amount must be greater than zero.")
        
        balance += amount
        print(f"Deposit successful! Your new balance is: ${balance:.2f}")
    
    except ValueError as ve:
        print(f"Error: {ve}")

# Function to withdraw money
def withdraw():
    global balance
    try:
        # Get withdrawal amount from the user
        amount = float(input("Enter amount to withdraw: "))
        
        if amount <= 0:
            raise ValueError("Withdrawal amount must be greater than zero.")
        
        if amount > balance:
            raise ValueError("Insufficient funds!")
        
        balance -= amount
        print(f"Withdrawal successful! Your new balance is: ${balance:.2f}")
    
    except ValueError as ve:
        print(f"Error: {ve}")

# Function to check balance
def check_balance():
    print(f"Your current balance is: ${balance:.2f}")

# Main function to run the banking system
def banking_system():
    while True:
        show_menu()  # Show the menu options
        try:
            choice = int(input("Select an option (1-4): "))
            
            if choice == 1:
                deposit()
            elif choice == 2:
                withdraw()
            elif choice == 3:
                check_balance()
            elif choice == 4:
                print("Thank you for using the banking system. Goodbye!")
                break
            else:
                print("Invalid option. Please choose a number between 1 and 4.")
        
        except ValueError:
            print("Error: Invalid input! Please enter a number between 1 and 4.")

# Start the banking system
banking_system()
