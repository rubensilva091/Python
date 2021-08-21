import tkinter as tk
from tkinter.constants import COMMAND
from typing import Collection
import pyperclip
import random
import json

LOGO_PNG = "d29 Password_Manager\logo.png"


root = tk.Tk()
root.config(pady=20, padx=20)
root.resizable(width=False, height=False)
root.title("Password Generator")


# functions


def save():
    with open("d29 Password_Manager\data.json", "r") as data_file:
        new_data = save_funct()
        json.dump(new_data, data_file, indent=4)


def save_funct():
    password = str(password_entry.get())
    email_username = str(email_username_entry.get())
    website = str(website_entry.get())

    new_data = {
        website: {
            "email": email_username,
            "password": password
        }
    }
    return new_data


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
               'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [random.choice(letters)
                        for _ in range(random.randint(8, 10))]
    password_symbols = [random.choice(symbols)
                        for _ in range(random.randint(2, 4))]
    password_numbers = [random.choice(numbers)
                        for _ in range(random.randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    random.shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)


# canvas
image_logo = tk.PhotoImage(file=LOGO_PNG)
logo = tk.Canvas(width=200, height=200)
logo.create_image(100, 100, image=image_logo)
logo.grid(row=0, column=1)


# labels

website_label = tk.Label(root, text="Website: ")
website_label.grid(row=1, column=0)


email_username_label = tk.Label(root, text="Email/Username: ")
email_username_label.grid(row=2, column=0)

password_label = tk.Label(root, text="Password: ")
password_label.grid(row=3, column=0)


# Entry

website_entry = tk.Entry(root, width=35)
website_entry.grid(row=1, column=1, columnspan=2)


email_default = tk.StringVar()
email_default.set("rubenfamalicao@live.com.pt")


email_username_entry = tk.Entry(root, width=35, textvariable=email_default)
email_username_entry.grid(row=2, column=1, columnspan=2)


password_entry = tk.Entry(root, width=21)
password_entry.grid(row=3, column=1)


# buttons

generate_password_button = tk.Button(
    root, text="Generate Password", command=generate_password)
generate_password_button.grid(row=3, column=2)

add_button = tk.Button(root, text="Add", width=36, command=save)
add_button.grid(row=4, column=1, columnspan=2)


root.mainloop()
