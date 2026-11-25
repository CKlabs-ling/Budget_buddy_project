class Budget:
    def __init__(self, expense_type):
        self.expense_types = expense_type
        self.expenses_dict = {}
        #self.expenses_list = []
        #self.catagories = []

    def add_expanse(self):
        while True:
            try:
                many_expense = int(input(f"how many {self.expense_types} expanses do you have? Enter an Integer:\n"))
                break
            except:
                print("**ERROR**\n---Try Again---\nEnter an Integer:")

        print("Enter input expenses in \"Type Cost\" format for e.g, Milk 10: ")
        for i in range(many_expense):
            while True:
                try:
                    type, exp = input(f"expense #{int(i+1)}:").split()
                    self.expenses_dict[type] = float(exp)

                    #self.expenses_list.append(float(user_expenses))
                    #self.catagories.append(type)
                    break
                except:
                    print("**ERROR**\nWRONG INPUT!!! Enter input expenses in \"Type Cost\" format for e.g, Milk 10:  ")
        self.write_to_file()

    def get_expanse(self):
        user_expenses_total = sum(self.expenses_dict.values())
        print(f"Total money you spend on {self.expense_types}: {user_expenses_total:.2f} ")
        return user_expenses_total

    def get_expence_detail(self):
        for type,exp in self.expenses_dict.items():
            print(f"    {type}: ${exp:.2f}")

    def write_to_file(self):
        with open("expense_data.txt", "a") as data:
            data.write(f"{self.expense_types}\n")

            for type,exp in self.expenses_dict.items():
                data.write(f"    {type}: ${exp:.2f}\n")

            data.write("\n")