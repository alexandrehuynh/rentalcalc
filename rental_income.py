class User:
    def __init__(self, name):
        self.name = name
        self.properties = []

    def add_property(self, property):
        self.properties.append(property)

    def remove_property(self, address):
        self.properties = [p for p in self.properties if p.address != address]

    def list_properties(self):
        if not self.properties:
            print("No properties found.")
            return
        for property in self.properties:
            print(f"Address: {property.address}")

class Property:
    def __init__(self, address):
        self.address = address
        self.expenses = []
        self.incomes = []
        self.roi = 0

    def add_expense(self, expense_name, expense_amount):
        self.expenses.append((expense_name, expense_amount))

    def remove_expense(self, expense_name):
        self.expenses = [expense for expense in self.expenses if expense[0] != expense_name]

    def add_income(self, income_name, income_amount):
        self.incomes.append((income_name, income_amount))

    def remove_income(self, income_name):
        self.incomes = [income for income in self.incomes if income[0] != income_name]

    def calculate_roi(self):
        total_expense = sum(amount for _, amount in self.expenses)
        total_income = sum(amount for _, amount in self.incomes)
        if total_expense > 0:
            self.roi = (total_income - total_expense) / total_expense * 100
        else:
            self.roi = 0
        return self.roi

    def list_incomes(self):
        return self.incomes

    def list_expenses(self):
        return self.expenses

class UserManager:
    def __init__(self):
        self.users = []

    def add_user(self):
        name = input("Enter the user's name: ")
        user = User(name)
        self.users.append(user)
        print(f"User {name} added successfully.")

    def select_user(self):
        if not self.users:
            print("No users available. Please add a user first.")
            return
        for i, user in enumerate(self.users):
            print(f"{i + 1}. {user.name}")
        try:
            user_index = int(input("Select a user: ")) - 1
            if 0 <= user_index < len(self.users):
                self.user_menu(self.users[user_index])
            else:
                print("Invalid user selection. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    def user_menu(self, user):
        while True:
            print("\nUser Menu")
            print("1. Add Property")
            print("2. List Properties")
            print("3. Calculate ROI for a Property")
            print("4. Return to Main Menu")

            choice = input("Enter your choice: ")

            if choice == "1":
                self.add_property(user)
            elif choice == "2":
                user.list_properties()
            elif choice == "3":
                self.calculate_roi(user)
            elif choice == "4":
                break
            else:
                print("Invalid choice. Please try again.")

    def add_property(self, user):
        address = input("Enter the property address: ").capitalize()
        # Check for unique address
        if any(p.address == address for p in user.properties):
            print("Property with this address already exists.")
            return
        property = Property(address)
        user.add_property(property)
        print(f"Property at {address} added successfully.")

    def calculate_roi(self, user):
        user.list_properties()
        if not user.properties:
            return
        address = input("Enter the address of the property to calculate ROI: ").capitalize()
        property = next((p for p in user.properties if p.address == address), None)
        if property is None:
            print("Property not found.")
            return
        total_expense = sum([float(input(f"Enter amount for {expense[0]}: ")) for expense in property.list_expenses()])
        total_income = sum([float(input(f"Enter amount for {income[0]}: ")) for income in property.list_incomes()])
        roi = property.calculate_roi()
        print(f"The ROI for the property at {property.address} is {roi:.2f}%.")

class Menu:
    def __init__(self, user_manager):
        self.user_manager = user_manager

    def main_menu(self):
        while True:
            print("\nRental Property Calculator")
            print("1. Add User")
            print("2. Select User")
            print("3. Exit")
            
            choice = input("Enter your choice: ")
            
            if choice == "1":
                self.user_manager.add_user()
            elif choice == "2":
                self.user_manager.select_user()
            elif choice == "3":
                print("Exiting program.")
                break
            else:
                print("Invalid choice. Please try again.")

user_manager = UserManager()
menu = Menu(user_manager)
menu.main_menu()
