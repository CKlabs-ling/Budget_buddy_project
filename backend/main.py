import os
from libary.backroom_functions import calc_balance, financial_status
from libary.classes import Budget

def display_menu():
    print("\n-=-=-=-=-= BudgetBuddy =-=-=-=-=-")
    print("\nWhat's next?")
    print("---------------------------------")
    print("Create a new expense category  ---> 1")
    print("Add expenses into category     ---> 2")
    print("Display expenses list          ---> 3")
    print("My financial status            ---> 4")
    print("Delete expense category        ---> 5")
    print("Delete individual expense      ---> 6")
    print("Exit program                   ---> 7")
    print("---------------------------------")

    selection = input("Your selection: ")
    return selection

Entername = input("Please Enter your name: ")
os.system("cls" if os.name == "nt" else "clear")

print(f"Hey {Entername}, this is BudgetBuddy! Your Personal Budgeting Assistant.")

while True:
    try:
        user_income = float(input("Enter monthly Income: "))
        break
    except ValueError:
        print("**ERROR**\n---Try Again---\nEnter an Integer:")

total_all_expanse = []
all_categories = []

if os.path.exists("expense_data.txt"):
    loader = Budget("")
    loader.load_all_categories()

    for category_name in loader.all_categories:
        category = Budget(category_name)
        all_categories.append(category)

    print("Welcome back! Your saved categories have been loaded.")

else:
    print("Welcome to BudgetBuddy!")
    print("Let's set up your first expense category.")

#category_amount = int(input("How many categories of expenses do you have? Enter an Integer: "))
#for i in range(category_amount):
    #category_name = input(f"Enter name of category #{int(i+1)}: ")
    #category_expense = Budget(category_name)
    #all_categories.append(category_expense)
    #category_expense.add_expanse()
    #exp_category = category_expense.get_expanse()
    #detail_category = category_expense.get_expence_detail()

    #total_all_expanse.append(exp_category)

for category in all_categories:
    category.get_expence_detail()

total_expense = sum(total_all_expanse)


#grocery = Budget("Grocery")
#car = Budget("Car")

#grocery.add_expanse()
#car.add_expanse()

#exp_grocery= grocery.get_expanse()
#detail_grocery = grocery.get_expence_detail()
#exp_car= car.get_expanse()
#detail_car = car.get_expence_detail()


#total_all_expanse.append(exp_grocery)
#total_all_expanse.append(exp_car)

balance = calc_balance(user_income, total_expense)
print(f"Total Balance: ${balance:.2f}")
financial_status(balance)

while True:
    choice = display_menu()

    if choice == "1":
        category_name = input("Enter the new category name: ")

        if category_name in [category.expense_types for category in all_categories]:
            print("This category already exists!")
        else:
            new_category = Budget(category_name)
            all_categories.append(new_category)
            new_category.write_to_file()

            print(f"{category_name} category created successfully!")

    elif choice == "2":
        if len(all_categories) == 0:
            print("No categories available. Create a category first.")

        else:
            print("\nAvailable Categories:")

            for i, category in enumerate(all_categories):
                print(f"{i + 1}. {category.expense_types}")

            try:
                selection = int(input("Select a category number: "))

                if selection >= 1 and selection <= len(all_categories):
                    selected_category = all_categories[selection - 1]
                    selected_category.add_expanse()
                else:
                    print("Invalid category number.")

            except ValueError:
                print("Please enter a valid number.")

    elif choice == "3":
        if len(all_categories) == 0:
            print("No categories available.")
        else:
            print("\n========== EXPENSES LIST ==========")

            for category in all_categories:
                category.display_saved_expenses()

    elif choice == "4":
        total_expense = 0

        for category in all_categories:
            category.expenses_dict = {}
            category.load_from_file()
            total_expense += sum(category.expenses_dict.values())

        balance = calc_balance(user_income, total_expense)

        print("\n========== FINANCIAL STATUS ==========")
        print(f"Monthly Income: ${user_income:.2f}")
        print(f"Total Expenses: ${total_expense:.2f}")
        print(f"Remaining Balance: ${balance:.2f}")

        financial_status(balance)

    elif choice == "5":
        if len(all_categories) == 0:
            print("No categories available.")

        else:
            print("\nAvailable Categories:")

            for i, category in enumerate(all_categories):
                print(f"{i + 1}. {category.expense_types}")

            try:
                selection = int(input("Select a category to delete: "))

                if 1 <= selection <= len(all_categories):
                    selected_category = all_categories[selection - 1]
                    selected_category.delete_category()
                    all_categories.remove(selected_category)
                else:
                    print("Invalid category number.")

            except ValueError:
                print("Please enter a valid number.")

    elif choice == "6":
        if len(all_categories) == 0:
            print("No categories available.")

        else:
            print("\nAvailable Categories:")

            for i, category in enumerate(all_categories):
                print(f"{i + 1}. {category.expense_types}")

            try:
                selection = int(input("Select a category: "))

                if 1 <= selection <= len(all_categories):
                    selected_category = all_categories[selection - 1]
                    selected_category.delete_expense()
                else:
                    print("Invalid category number.")

            except ValueError:
                print("Please enter a valid number.")


    elif choice == "7":
        print("Thank you for using BudgetBuddy!")
        break

    else:
        print("Invalid selection. Please choose an option from 1-7.")