from tkinter import *
import pandas
from tkinter import messagebox, simpledialog
import pyperclip
from sys import exit

pin = simpledialog.askstring("Log in.", "                        Enter pin:                         ", show="*")
pin = int(pin)

if pin != 1234:
    exit()

# TRIES TO READ FROM THE SAVE FILE IF IT EXISTS
try:
    accounts_data = pandas.read_csv("accounts_data.csv")

    username_list = accounts_data["username"].to_list()
    website_list = accounts_data["website"].to_list()
    password_list = accounts_data["password"].to_list()
    data_dict = {
        "username": username_list,
        "website": website_list,
        "password": password_list,
    }
# MAKES A SAVE FILE IF THERE IS NONE ONLY TRIGGERS IF TRY FAILS
except:
    with open("accounts_data.csv", 'w') as file:
        data_dict = {
            "username": [],
            "website": [],
            "password": []
        }
        pandas.DataFrame(data_dict).to_csv("accounts_data.csv")

# FUNCTIONS

# Save function to save credentials to file when add button is clicked


def save():
    website = website_entry.get()
    username = username_entry.get()
    password = password_entry.get()

    if len(website) == 0 or len(username) == 0:
        messagebox.showwarning(title="Ooops", message="You can't leave any fields empty.")

    else:

        is_ok = messagebox.askokcancel(title=website, message=f"These are your credentials:\n"
                                                              f"Email/Username: {username}\n"
                                                              f"Password: {password}\n"
                                                              f"Is this ok?")
        if is_ok:
            with open("accounts_data.csv", "w") as file_data:
                data_dict["website"] += [website]
                data_dict["username"] += [username]
                data_dict["password"] += [password]
                data_df = pandas.DataFrame(data_dict)
                data_df.to_csv("accounts_data.csv")
                website_entry.delete(0, END)
                password_entry.delete(0, END)
                website_entry.focus()


# Functions to switch between frames


def switch_to_frame1():
    frame2.grid_forget()  # Hide frame2
    frame1.grid(row=0, column=0, sticky='nsew')  # Show frame1

# Also generates buttons and entries in frame 2
def switch_to_frame2():
    accounts = pandas.read_csv("accounts_data.csv")

    r = 1
    for account in accounts.website:
        button = Button(frame2, text=account, width=13)
        button.grid(column=0, row=r)
        r += 1

    r = 1

    for password in accounts.password:
        entry = Entry(frame2, width=22, justify="center")
        entry.insert(0, password)
        entry.grid(column=1, row=r)
        r += 1
    frame1.grid_forget()  # Hide frame1
    frame2.grid(row=0, column=0, sticky='nsew')  # Show frame2


# FUNCTION TO GENERATE A RANDOM PASSWORD


def generate():
    import random
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]

    password_list = password_numbers + password_symbols + password_letters
    random.shuffle(password_list)

    password = "".join(password_list)
    pyperclip.copy(password)

    password_entry.delete(0, END)
    password_entry.insert(0, password)

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

# Entries for first frame
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

# Buttons for first frame
generate_button = Button(frame1, text="Generate password", command=generate)
generate_button.grid(column=2, row=3)

add_button = Button(frame1, text="Add", width=30, command=save)
add_button.grid(column=1, row=4, columnspan=2)

get_password_button = Button(frame1, text="Get passwords...", width=30, command=switch_to_frame2)
get_password_button.grid(column=1, row=5, columnspan=2)

# Labels and buttons for second frame
accounts_label = Label(frame2, text="Accounts:", font=("", 13))
accounts_label.grid(column=0, row=0)
passwords_label = Label(frame2, text="Passwords:", font=("", 13))
passwords_label.grid(column=1, row=0, pady=20)
back_button = Button(frame2, text="Back", command=switch_to_frame1)
back_button.grid(column=2)

frame1.grid(row=0, column=0, sticky='nsew')

window1.mainloop()
