import pandas
from tkinter import *

r = 1

window2 = Toplevel()
window2.title("Password manager")
window2.config(padx=50, pady=50)

label = Label(text="Existing accounts", font=("courier", 15))
label.grid(column=1, row=0)

accounts = pandas.read_csv("accounts_data.csv")

for account in accounts.website:
    button = Button(text=account, width=13)
    button.grid(column=0, row=r)
    r += 1

r = 1

for password in accounts.password:
    label = Label(text=password, width=25)
    label.grid(column=1, row=r)
    r += 1



window.mainloop()