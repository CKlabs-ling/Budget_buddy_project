from tkinter import *
from frontend.frontroom_function import *

window = Tk() #make the window
window.geometry("1280x720")
window.title("CAT's BudgetBuddy")

user_entry = Entry(window,
                   font = ("Arial", 30),
                   width = 25)
user_entry.pack(side = LEFT)

Enter_bt = Button(window,
                  text = "submit",
                  command = submit)
Enter_bt.pack(side = RIGHT)

delete_bt = Button(window,
                  text = "Delete",
                  command = delete)
delete_bt.pack(side = RIGHT)

backspace_bt = Button(window,
                  text = "Backspace",
                  command = backspace)
backspace_bt.pack(side = RIGHT)

window.mainloop()#place window on screen