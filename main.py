from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

window = Tk()
window.config(padx=50, pady=50)
window.title("Password Manager")


def search_result():
    search_for = website_entry.get()
    try:
        with open("data.json") as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showerror(title="ERROR", message="Data File Not Found")
    else:
        try:
            messagebox.showinfo(title=search_for, message=f"Email: {data[search_for]["username"]}\n"
                                                          f"Password: {data[search_for]["password"]}")
        except KeyError:
            messagebox.showerror(title="ERROR", message="No Data Available.")


def password_generator():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [random.choice(letters) for _ in range(random.randint(8, 10))]
    password_symbols = [random.choice(symbols) for _ in range(random.randint(2, 4))]
    password_numbers = [random.choice(numbers) for _ in range(random.randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers

    random.shuffle(password_list)

    generated_password = ''.join(password_list)
    pyperclip.copy(generated_password)

    password_entry.insert(0, generated_password)


def saving_data():
    website = website_entry.get()
    username = username_entry.get()
    password = password_entry.get()

    def clear_entry():
        website_entry.delete(0, END)
        username_entry.delete(0, END)
        password_entry.delete(0, END)
        website_entry.focus()

    new_data_dict = {
        website: {
            "username": username,
            "password": password,
        }
    }

    if website == "" or username == "" or password == "":
        messagebox.showwarning(title="WARNING", message="Do not leave any field empty.")

    else:
        try:
            with open("data.json", mode="r") as file:
                data = json.load(file)
        except FileNotFoundError:
            with open("data.json", mode="w") as file:
                json.dump(new_data_dict, file, indent=4)
                clear_entry()
        else:
            data.update(new_data_dict)
            with open("data.json", mode="w") as file:
                json.dump(data, file, indent=4)
                clear_entry()


canvas = Canvas(width=200, height=200, highlightthickness=0)
canvas.grid(row=0, column=1)
pass_photo = PhotoImage(file="logo.png")
canvas.create_image(120, 100, image=pass_photo)

website_label = Label()
website_label.config(text="Website: ")
website_label.grid(row=1, column=0)

website_entry = Entry(width=36)
website_entry.focus()
website_entry.grid(row=1, column=1)

search_button = Button(text="Search", width=13, command=search_result)
search_button.grid(row=1, column=2)

username_label = Label()
username_label.config(text="Email/Username: ")
username_label.grid(row=2, column=0)

username_entry = Entry(width=54)
username_entry.grid(row=2, column=1, columnspan=2)

password_label = Label()
password_label.config(text="Password: ")
password_label.grid(row=3, column=0)

password_entry = Entry(width=36)
password_entry.grid(row=3, column=1)

generate_password = Button(text="Generate Password", command=password_generator)
generate_password.grid(row=3, column=2)

add_button = Button(text="Add", width=52, command=saving_data)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
