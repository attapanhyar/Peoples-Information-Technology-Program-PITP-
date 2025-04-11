class Restaurant:
    def __init__(self):
        self.menu = {
            "Burger": 5.99,
            "Fries": 2.99,
            "Soda": 1.99,
            "Salad": 4.99,
            "Chicken Nuggets": 6.99,
        }
        self.order_total = 0

    def display_menu(self):
        print("Menu:")
        for item, price in self.menu.items():
            print(f"{item}: ${price:.2f}")

    def get_order(self):
        while True:
            order = input("What would you like to order? ").title()
            if order in self.menu:
                print(f"Great choice! That'll be ${self.menu[order]:.2f}.")
                self.order_total += self.menu[order]
                break
            else:
                print("Sorry, we don't have that item. Please try again.")

    def run(self):
        print("Welcome to Sumia Restaurant!")
        while True:
            self.display_menu()
            self.get_order()
            cont = input("Would you like to order again? (y/n) ")
            if cont.lower() != "y":
                print(f"Your total is: ${self.order_total:.2f}")
                print("Thank you for dining with us! Goodbye!")
                break

if __name__ == "__main__":
    restaurant = Restaurant()
    restaurant.run()