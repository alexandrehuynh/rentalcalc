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
    def __init__(self, address, initial_investment):
        self.address = address
        self.initial_investment = initial_investment
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
    
    def calculate_total_income(self):
        return sum(amount for _, amount in self.incomes)

    def calculate_total_expenses(self):
        return sum(amount for _, amount in self.expenses)

    def calculate_cash_flow(self):
        return self.calculate_total_income() - self.calculate_total_expenses()

    def calculate_cash_on_cash_roi(self):
        cash_flow_annual = self.calculate_cash_flow() * 12
        if self.initial_investment > 0:
            return (cash_flow_annual / self.initial_investment) * 100
        else:
            return 0

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
            print("\n--- User Menu ---")
            print("1. Add Property")
            print("2. List Properties")
            print("3. Calculate ROI for a Property")
            print("4. Return to Main Menu")
            print("5. Exit Program")
            choice = input("Enter your choice: ")

            if choice == "1":
                self.add_property(user)
            elif choice == "2":
                user.list_properties()
            elif choice == "3":
                self.calculate_roi(user)
            elif choice == "4":
                break
            elif choice == "5":
                exit()
            else:
                print("Invalid choice. Please try again.")

    def add_property(self, user):
        print("\n--- Add a New Property ---")
        address = input("Enter the property address (e.g., '123 Main St'): ").strip().title()
        if any(p.address == address for p in user.properties):
            print("Property with this address already exists.")
            return
        print("Enter the initial investment amount (e.g., 50000 for $50,000):")
        try:
            initial_investment = float(input("Initial Investment: $"))
        except ValueError:
            print("Invalid amount. Please enter a number.")
            return

        property = Property(address, initial_investment)
        self.add_financials(property)
        user.add_property(property)
        print(f"Property at {address} added successfully.")
    
    def add_financials(self, property):
        print("\n--- Add Income Sources ---")
        print("Enter monthly income sources and amounts (e.g., 'Rent 2400'). Type 'done' to finish.")
        while True:
            income_input = input("Income Source (Name Amount): ")
            if income_input.lower() == 'done':
                break
            try:
                income_name, income_amount = income_input.split(maxsplit=1)
                income_amount = float(income_amount)
                property.add_income(income_name.strip().capitalize(), income_amount)
            except ValueError:
                print("Invalid format. Please enter as 'Name Amount'.")

        print("\n--- Add Expense Items ---")
        print("Enter monthly expense items and amounts (e.g., 'Mortgage 1100'). Type 'done' to finish.")
        while True:
            expense_input = input("Expense Item (Name Amount): ")
            if expense_input.lower() == 'done':
                break
            try:
                expense_name, expense_amount = expense_input.split(maxsplit=1)
                expense_amount = float(expense_amount)
                property.add_expense(expense_name.strip().capitalize(), expense_amount)
            except ValueError:
                print("Invalid format. Please enter as 'Name Amount'.")

    def calculate_roi(self, user):
        if not user.properties:
            print("No properties available. Please add a property first.")
            return
        for i, property in enumerate(user.properties):
            print(f"{i + 1}. {property.address}")
        try:
            property_index = int(input("Select a property number to calculate ROI: ")) - 1
            if 0 <= property_index < len(user.properties):
                property = user.properties[property_index]
            else:
                print("Invalid property selection. Please try again.")
                return
        except ValueError:
            print("Invalid input. Please enter a number.")
            return

        total_income = property.calculate_total_income()
        total_expenses = property.calculate_total_expenses()
        cash_flow = property.calculate_cash_flow()
        cash_on_cash_roi = property.calculate_cash_on_cash_roi()

        print(f"\nFinancial Overview for {property.address}:")
        print(f"Total Income: {total_income}")
        print(f"Total Expenses: {total_expenses}")
        print(f"Cash Flow: {cash_flow}")
        print(f"Cash on Cash ROI: {cash_on_cash_roi:.2f}%")

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
