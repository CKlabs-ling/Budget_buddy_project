class Budget:
    def __init__(self, expense_type):
        self.expense_types = expense_type
        self.expenses_dict = {}
        #self.expenses_list = []
        #self.catagories = []

    def load_all_categories(self):
        self.all_categories = {}

        try:
            with open("expense_data.txt", "r") as data:
                lines = data.readlines()

            current_category = None

            for line in lines:
                line = line.strip()

                if line == "":
                    current_category = None

                elif ": $" not in line:
                    current_category = line

                    if current_category not in self.all_categories:
                        self.all_categories[current_category] = {}
                else:
                    if current_category is not None:
                        expense_type, cost = line.split(": $")
                        expenses = self.all_categories[current_category]
                        expenses[expense_type] = expenses.get(expense_type, 0) + float(cost)

        except FileNotFoundError:
            self.all_categories = {}

    def display_saved_expenses(self):
        self.expenses_dict = {}
        self.load_from_file()

        print(f"\n{self.expense_types}:")

        if not self.expenses_dict:
            print("    No expenses recorded yet.")
        else:
            self.get_expence_detail()
            total = sum(self.expenses_dict.values())
            print(f"    Total: ${total:.2f}")

    def load_from_file(self):
        try:
            with open("expense_data.txt", "r") as data:
                lines = data.readlines()

            reading_category = False

            for line in lines:
                line = line.strip()

                if line == self.expense_types:
                    reading_category = True

                elif line == "":
                    reading_category = False

                elif reading_category:
                    expense_type, cost = line.split(": $")
                    self.expenses_dict[expense_type] = (
                        self.expenses_dict.get(expense_type, 0) + float(cost)
                    )

        except FileNotFoundError:
            self.expenses_dict = {}
    
    def add_expanse(self):
        self.load_from_file() 
        
        while True:
            try:
                many_expense = int(input(f"How many {self.expense_types} expenses do you have? Enter an Integer:\n"))
                break
            except ValueError:
                print("**ERROR**\n---Try Again---\nEnter an Integer:")

        print("Enter input expenses in \"Type Cost\" format for e.g, Milk 10: ")
        for i in range(many_expense):
            while True:
                try:
                    type, exp = input(f"Expense #{int(i+1)}: ").split()
                    #self.expenses_dict[type] = float(exp)
                    self.expenses_dict[type] = self.expenses_dict.get(type, 0) + float(exp)

                    #self.expenses_list.append(float(user_expenses))
                    #self.catagories.append(type)
                    break
                except ValueError:
                    print("**ERROR**\nWRONG INPUT!!! Enter input expenses in \"Type Cost\" format for e.g, Milk 10:  ")
        self.write_to_file()

    def get_expanse(self):
        user_expenses_total = sum(self.expenses_dict.values())
        print(f"Total money you spent on {self.expense_types}: ${user_expenses_total:.2f} ")
        return user_expenses_total

    def get_expence_detail(self):
        for type,exp in self.expenses_dict.items():
            print(f"    {type}: ${exp:.2f}")

    def delete_category(self):
        self.load_all_categories()

        if self.expense_types not in self.all_categories:
            print("Category not found.")
            return

        del self.all_categories[self.expense_types]

        with open("expense_data.txt", "w") as data:
            for category, expenses in self.all_categories.items():
                data.write(f"{category}\n")

                for expense, cost in expenses.items():
                    data.write(f"{expense}: ${cost:.2f}\n")

                data.write("\n")

        print(f"{self.expense_types} category deleted successfully!")

    def delete_expense(self):
        self.expenses_dict = {}
        self.load_from_file()

        if not self.expenses_dict:
            print("No expenses available in this category.")
            return

        print(f"\nExpenses in {self.expense_types}:")

        expense_list = list(self.expenses_dict.keys())

        for i, expense in enumerate(expense_list):
            print(f"{i + 1}. {expense}: ${self.expenses_dict[expense]:.2f}")

        try:
            selection = int(input("Select an expense to delete: "))

            if 1 <= selection <= len(expense_list):
                selected_expense = expense_list[selection - 1]

                del self.expenses_dict[selected_expense]

                self.write_to_file()

                print(f"{selected_expense} deleted successfully!")

            else:
                print("Invalid expense number.")

        except ValueError:
            print("Invalid input. Please enter a valid expense number.")

    def write_to_file(self):
        self.load_all_categories()

        self.all_categories[self.expense_types] = self.expenses_dict.copy()

        with open("expense_data.txt", "w") as data:
            for category, expenses in self.all_categories.items():
                data.write(f"{category}\n")

                for expense, cost in expenses.items():
                    data.write(f"{expense}: ${cost:.2f}\n")

                data.write("\n")