from tkinter import *

window = Tk()
window.title("My first GUI Program")
window.minsize(width=500, height=300)

# Label
my_label = Label(text= "I am a label", font=("Arial", 24, "italic"))
my_label.pack()

my_label["text"] = "New Text"
my_label.config(text="New Text")

# Button

def button_clicked():
    # my_label.config(text="Button got clicked")
    my_label.config(text=f"{input.get()}")

button = Button(text="Click Me", command=button_clicked)
button.pack()

# Entry
input = Entry(width=10)
input.pack()
print(input.get())

window.mainloop()

# def add(*args):
#     print(args[1])
#     sum = 0
#     for n in args:
#         sum += n
#     return sum
#
# print(add(1,2,3,4,5))
#
# def calculate(n, **kwargs):
#     print(kwargs)
#     # for key, value in kwargs.items():
#     #     print(key)
#     #     print(value)
#     n += kwargs["add"]
#     n *= kwargs["multiply"]
#     print(n)
#
# calculate(2, add=3, multiply=5)
#
# # Use .get("") instead of [""] because .get() returns none when "" doesn't exist