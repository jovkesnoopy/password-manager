from tkinter import *
import pandas

accounts_data = pandas.read_csv("accounts_data.csv")

username_list = accounts_data["username"].to_list()
website_list = accounts_data["website"].to_list()
password_list = accounts_data["password"].to_list()
data_dict = {
    "username": username_list,
    "website": website_list,
    "password": password_list,
}

# Functions


def save():
    data_dict["website"] += [website_entry.get()]
    data_dict["username"] += [username_entry.get()]
    data_dict["password"] += [password_entry.get()]
    data_df = pandas.DataFrame(data_dict)
    data_df.to_csv("accounts_data.csv")
    website_entry.delete(0, END)
    password_entry.delete(0, END)
    website_entry.focus()


def switch_to_frame1():
    frame2.grid_forget()  # Hide frame2
    frame1.grid(row=0, column=0, sticky='nsew')  # Show frame1


def switch_to_frame2():
    frame1.grid_forget()  # Hide frame1
    frame2.grid(row=0, column=0, sticky='nsew')  # Show frame2


# def show_passwords():
# ---- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #


window1 = Tk()
window1.title("Password manager")
window1.config(padx=50, pady=50)
frame1 = Frame(window1)
frame2 = Frame(window1)
logo = PhotoImage(file="logo.png")
canvas = Canvas(width=200, height=200)
canvas.create_image(100, 100, image=logo)
canvas.grid(column=1, row=0)

# Entries
website_entry = Entry(frame1, width=35)
website_entry.grid(column=1, row=1, columnspan=2)
website_entry.focus()

username_entry = Entry(frame1, width=35)
username_entry.grid(columnspan=2, column=1, row=2)
username_entry.insert(0, "s.jovanovic12@yahoo.com")

password_entry = Entry(frame1, width=17, show="*")
password_entry.grid(column=1, row=3)

# Labels
website_label = Label(frame1, text="Website:")
website_label.config(padx=10)
website_label.grid(column=0, row=1)

username_label = Label(frame1, text="email/Username:")
username_label.grid(column=0, row=2)

password_label = Label(frame1, text="Password:")
password_label.grid(column=0, row=3)


# Buttons
generate_button = Button(frame1, text="Generate password")
generate_button.grid(column=2, row=3)

add_button = Button(frame1, text="Add", width=30, command=save)
add_button.grid(column=1, row=4, columnspan=2)

get_password_button = Button(frame1, text="Get password...", width=30, command=switch_to_frame2)
get_password_button.grid(column=1, row=5, columnspan=2)


label = Label(frame2, text="Existing accounts", font=("courier", 15))
label.grid(column=1, row=0)
back_button = Button(frame2, text="Back", command=switch_to_frame1)
back_button.grid(column=2)


# Generate buttons and labels with names from dictionary

accounts = pandas.read_csv("accounts_data.csv")

r = 1
for account in accounts.website:
    button = Button(frame2, text=account, width=13)
    button.grid(column=0, row=r)
    r += 1

r = 1

for password in accounts.password:
    label = Label(frame2, text=password, width=25)
    label.grid(column=1, row=r)
    r += 1

frame1.grid(row=0, column=0, sticky='nsew')

# Configure grid weights to make frames expand with the window
window1.grid_rowconfigure(0, weight=1)
window1.grid_columnconfigure(0, weight=1)








window1.mainloop()