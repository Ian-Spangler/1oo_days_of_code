# Higer-Lower
from flask import Flask
import random

app = Flask(__name__)

random_number = random.randint(0,9)

@app.route("/")
def home():
    return '<h1 style="text-align: center">Guess a number between 0 and 9</h1>' \
    '<img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif"></img>'

@app.route("/<int:number>")
def guess(number):
    if random_number > number:
        return '<h1>Too low, try again!</h1>' \
        '<img src="https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif"></img>'
    elif random_number < number:
        return '<h1>Too high, try again!</h1>' \
        '<img src="https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif"></img>'
    else:
        return '<h1>You found me!</h1>' \
        '<img src="https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif"></img>'

if __name__ == "__main__":
    app.run(debug=True)