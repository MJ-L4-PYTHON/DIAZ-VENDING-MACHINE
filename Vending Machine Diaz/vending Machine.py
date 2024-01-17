class VendingMachine:
    def __init__(self):
        # Define the menu with categories
        self.menu = {
            'Hot Drinks': {'Hot Chocolate': 1.50, 'Coffee': 1.00, 'tea': 2.00, 'Chai': 3.00},
            'Cold Drinks': {'Iced Coffee': 3.50, 'Strawberry Juice': 2.50, 'Chocolate Milk': 4.00},
            'Soft Drinks': {'Fanta': 4.50, 'Coke': 5.00, 'Sprite': 3.00, 'Mountain Dew': 6.00},
            'Snacks': {'Chips': 7.50, 'Pocky Sticks': 5.00, 'Cookies': 1.50, 'Mochi': 5.00, 'Ice cream': 10.00},
            'Candies': {'Gummy Bears': 1.50, 'Chocolate Bar': 1.75, 'Lollipops': 1.00}
        }
        self.balance = 0.0  # User's money balance

    def display_menu(self):
        # Display the menu to the user
        print("==== VENDING MACHINE MENU ====")
        for category, items in self.menu.items():
            print(f"\n{category}:")
            for item, price in items.items():
                print(f"{item} - ${price:.2f}")

    def get_user_input(self):
        # Get user input for item selection
        codes = input("\nEnter the codes of the items you want to buy (separated by spaces): ").split()
        return codes

    def process_purchase(self, codes):
        # Process the user's multiple purchases
        total_cost = 0.0
        items_purchased = []

        for code in codes:
            for category, items in self.menu.items():
                if code in items:
                    item_name = items[code]
                    item_price = self.menu[category][code]

                    # Check if user has enough balance
                    if self.balance >= item_price:
                        self.balance -= item_price
                        total_cost += item_price
                        items_purchased.append(item_name)
                    else:
                        print("\nInsufficient funds. Please add more money.")
                        return

        if items_purchased:
            print("\nDispensing items:")
            for item in items_purchased:
                print(f"- {item}")
            print(f"Total Cost: ${total_cost:.2f}")
            print(f"Change: ${self.balance:.2f}")

    def add_money(self):
        # Allow user to add money to their balance
        amount = float(input("\nEnter the amount of money you want to add: $"))
        self.balance += amount
        print(f"Current balance: ${self.balance:.2f}")

    def run_vending_machine(self):
        # Main function to run the vending machine
        while True:
            self.display_menu()
            print("\nOptions:")
            print("1. Buy items")
            print("2. Add money")
            print("3. Exit")

            option = input("Choose an option (1/2/3): ")

            if option == '1':
                item_codes = self.get_user_input()
                self.process_purchase(item_codes)
            elif option == '2':
                self.add_money()
            elif option == '3':
                print("Exiting the vending machine. Thank you for using!")
                break
            else:
                print("Invalid option. Please choose a valid option.")


# Instantiate the vending machine
vending_machine = VendingMachine()

# Run the vending machine
vending_machine.run_vending_machine()