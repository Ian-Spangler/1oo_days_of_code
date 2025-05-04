from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return '<h1 style="text-align: center">Hello, World!</h1>' \
    '<p>This is a paragraph.</p>'

def make_bold(function):
    def wrapper():
        return f'<b>{function()}</b>'
    return wrapper

def make_emphasis(function):
    def wrapper():
        return f'<em>{function()}</em>'
    return wrapper

def make_underlined(function):
    def wrapper():
        return f'<u>{function()}</u>'
    return wrapper

@app.route("/bye")
@make_bold
@make_emphasis
@make_underlined
def say_bye():
    return "<p>Bye</p>"

if __name__ == "__main__":
    app.run(debug=True)