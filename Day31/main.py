from idlelib.outwin import file_line_pats

BACKGROUND_COLOR = "#B1DDC6"

from tkinter import *
import pandas
import random

def new_card():
    global current_word, flip_timer
    window.after_cancel(flip_timer)
    current_word = random.choice(french_english_dict)
    canvas.itemconfig(card_image, image=front_image)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_word["French"], fill="black")
    flip_timer = window.after(3000, func=flip_card)

def flip_card():
    global current_word
    canvas.itemconfig(card_image, image=back_image)
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_word["English"], fill="white")

def update_list():
    global current_word
    french_english_dict.remove(current_word)
    data_frame = pandas.DataFrame(french_english_dict)
    data_frame.to_csv("words_to_learn.csv", index=False)
    new_card()

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, func=flip_card)

try:
    data = pandas.read_csv("words_to_learn.csv")
except FileNotFoundError:
    data = pandas.read_csv("data/french_words.csv")
finally:
    french_english_dict = data.to_dict(orient="records")

current_word = {}

# Card
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
front_image = PhotoImage(file="images/card_front.png")
back_image = PhotoImage(file="images/card_back.png")
card_image = canvas.create_image(400, 263, image=front_image)
card_title = canvas.create_text(400, 150, text="", font=("Arial", 40, "italic"), fill="black")
card_word = canvas.create_text(400, 263, text="", font=("Arial", 60, "bold"), fill="black")
canvas.grid(column=0, row=0, columnspan=2)

new_card()

# Cross button
cross_image = PhotoImage(file="images/wrong.png")
cross_button = Button(image=cross_image, highlightthickness=0, command=new_card)
cross_button.grid(column=0, row=1)

# Check button
check_image = PhotoImage(file="images/right.png")
check_button = Button(image=check_image, highlightthickness=0, command=update_list)
check_button.grid(column=1, row=1)


window.mainloop()
