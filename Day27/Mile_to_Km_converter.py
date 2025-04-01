from tkinter import *

window = Tk()
window.title("Mile to KM converter")
window.config(padx=20, pady=20)

def label_generator(word, col, r):
    label = Label(text=word)
    label.grid(column=col, row=r)

def calculate():
    km = float(user_input.get()) * 1.609
    label_generator(f"{round(km, 1)}", 1, 1)

user_input = Entry(width=8)
user_input.grid(column=1, row=0)

label_generator("Miles", 2, 0)
label_generator("is equal to", 0, 1)
label_generator("Km", 2, 1)

button = Button(text="Calculate", command=calculate)
button.grid(column=1, row=2)

window.mainloop()