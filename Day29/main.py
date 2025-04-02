from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
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
    if len(website_link.get()) == 0 or len(password.get()) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")
    else:
        is_ok = messagebox.askokcancel(title=website_link.get(), message=f"These are the details entered: \nEmail:{email_username.get()} "
                           f"\nPassword: {password.get()} \nIs it ok to save?")
        if is_ok:
            with open("data.txt", "a") as data:
                data.write(f"{website_link.get()}  | {email_username.get()} | {password.get()}\n")
                website_link.delete(0, END)
                password.delete(0, END)


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
website_link = Entry(width=35)
website_link.grid(column=1, row=1, columnspan=2)
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

window.mainloop()

