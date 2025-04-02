from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def password_generator():
    # Password Generator Project
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = randint(8, 10)
    nr_symbols = randint(2, 4)
    nr_numbers = randint(2, 4)

    password_letters = [choice(letters) for char in range(nr_letters)]
    password_symbols = [choice(symbols) for char in range(nr_symbols)]
    password_numbers = [choice(numbers) for char in range(nr_numbers)]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    generated_password = "".join(password_list)
    password.delete(0, END)
    password.insert(0, generated_password)

    pyperclip.copy(generated_password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    new_data = {
        website_link.get(): {
            "email": email_username.get(),
            "password": password.get(),
        }
    }
    if len(website_link.get()) == 0 or len(password.get()) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")
    else:
        try:
            with open("data.json", "r") as data:
                # Reading old data
                old_data = json.load(data)
        except FileNotFoundError:
            with open("data.json", "w") as data:
                json.dump(new_data, data, indent=4)
        else:
            # Updating old data with new data
            old_data.update(new_data)

            with open("data.json", "w") as data:
                # Saving updated data
                json.dump(old_data, data, indent=4)
        finally:
            website_link.delete(0, END)
            password.delete(0, END)

# ---------------------------- SEARCH ------------------------------- #
def search():
    website = website_link.get()
    try:
        with open("data.json", "r") as data:
            existing_data = json.load(data)
    except KeyError:
        messagebox.showinfo(title="Error", message="No Data File Found.")
    else:
        if website in existing_data:
            existing_email = existing_data[website]["email"]
            existing_password = existing_data[website]["password"]
            messagebox.showinfo(title=website,
                                message=f"Email: {existing_data[website]["email"]}\n"
                                        f"Password: {existing_data[website]["password"]}")
            email_username.delete(0, END)
            password.delete(0, END)
            email_username.insert(0, existing_email)
            password.insert(0, existing_password)
        else:
            messagebox.showinfo(title="Error", message=f"No details for {website} exists.")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
photo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=photo)
canvas.grid(column=1, row=0)

# Labels
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)
email_username_label = Label(text="Email/Username:")
email_username_label.grid(column=0, row=2)
password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

# Entries
website_link = Entry(width=21)
website_link.grid(column=1, row=1)
website_link.focus()
email_username = Entry(width=35)
email_username.grid(column=1, row=2, columnspan=2)
email_username.insert(0, "ian_random_email@gmail.com")
password = Entry(width=21)
password.grid(column=1, row=3)

# Buttons
generate_password_button = Button(text="Generate Password", command=password_generator)
generate_password_button.grid(column=2, row=3)
add_button = Button(text="Add", width=36, command=save_password)
add_button.grid(column=1, row=4, columnspan=2)
search_button = Button(text="Search", width=13, command=search)
search_button.grid(column=2, row=1)
window.mainloop()

