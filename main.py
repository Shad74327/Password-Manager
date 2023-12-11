from tkinter import *
from tkinter import messagebox
import random
import pyperclip

window = Tk()
window.config(padx=50, pady=50)
window.title("Password Manager")

def password_generator():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [random.choice(letters) for letter in range(random.randint(8, 10))]
    password_symbols = [random.choice(symbols) for symbol in range(random.randint(2, 4))]
    password_numbers = [random.choice(numbers) for number in range(random.randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers

    random.shuffle(password_list)

    generated_password = ''.join(password_list)
    pyperclip.copy(generated_password)

    password_entry.insert(0, generated_password)


def saving_data():
    website = website_entry.get()
    username = username_entry.get()
    password = password_entry.get()

    if website == "" or username == "" or password == "":
        messagebox.showwarning(title="WARNING", message="Do not leave any field empty.")

    else:
        message = messagebox.askokcancel(title=website, message=f"Email: {username}\n Password: {password}\n "
                                                                f"Do you want to save it?")
        if message:
            with open("data.txt", mode="a") as file:
                file.write(f"{website} | {username} | {password}\n")
                website_entry.delete(0, END)
                username_entry.delete(0, END)
                password_entry.delete(0, END)
                website_entry.focus()


canvas = Canvas(width=200, height=200, highlightthickness=0)
canvas.grid(row=0, column=1)
pass_photo = PhotoImage(file="logo.png")
canvas.create_image(120, 100, image=pass_photo)

website_label = Label()
website_label.config(text="Website: ")
website_label.grid(row=1, column=0)

website_entry = Entry(width=56)
website_entry.focus()
website_entry.grid(row=1, column=1, columnspan=2)

username_label = Label()
username_label.config(text="Email/Username: ")
username_label.grid(row=2, column=0)

username_entry = Entry(width=56)
username_entry.grid(row=2, column=1, columnspan=2)

password_label = Label()
password_label.config(text="Password: ")
password_label.grid(row=3, column=0)

password_entry = Entry(width=38)
password_entry.grid(row=3, column=1)

generate_password = Button(text="Generate Password", command=password_generator)
generate_password.grid(row=3, column=2)

add_button = Button(text="Add", width=54, command=saving_data)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
