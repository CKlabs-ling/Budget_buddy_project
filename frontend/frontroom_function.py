from tkinter import *

def submit(user_entry):
    entername = user_entry.get()
    print(f"Hey {entername}, this is BudgetBuddy! Your Personal Budgeting Assistant.")
    user_entry.config(state = DISABLED)

def delete(user_entry):
    user_entry.delete(0,END)

def backspace(user_entry):
    user_entry.delete(len(user_entry.get())-1 ,END)
