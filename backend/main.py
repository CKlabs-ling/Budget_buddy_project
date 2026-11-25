import os
from libary.functions import calc_balance, financial_status
from libary.classes import Budget

Entername = input("Please Enter your name: ")
os.system("cls" if os.name == "nt" else "clear")

print(f"Hey {Entername}, this is BudgetBuddy! Your Personal Budgeting Assistant.")

user_income = float(input("Enter monthly Income: "))

grocery = Budget("Grocery")
car = Budget("Car")

grocery.add_expanse()
car.add_expanse()

exp_grocery= grocery.get_expanse()
detail_grocery = grocery.get_expence_detail()
exp_car= car.get_expanse()
detail_car = car.get_expence_detail()

total_all_expanse = []
total_all_expanse.append(exp_grocery)
total_all_expanse.append(exp_car)

balance = calc_balance(user_income, sum(total_all_expanse))
print(f"Total Balance: {balance:.2f}")
financial_status(balance)


