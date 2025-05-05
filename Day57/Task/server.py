from flask import Flask
from flask import render_template
import random
import datetime as dt
import requests

app = Flask(__name__)

@app.route("/")
def home():
    random_number = random.randint(1, 10)
    date = dt.datetime.now().year
    return render_template("index.html", num=random_number, year=date)

@app.route("/guess/<name>")
def guess(name):
    gender_response = requests.get(url=f"https://api.genderize.io?name={name}")
    gender = gender_response.json()["gender"]
    age_response = requests.get(url=f"https://api.agify.io?name={name}")
    age = age_response.json()["age"]
    return render_template("guess.html", user_name=name, guess_gender = gender, guess_age=age)

@app.route("/blog/<num>")
def get_blog(num):
    print(num)
    response = requests.get(url="https://api.npoint.io/e48b4506113776159935")
    all_posts = response.json()
    return render_template("blog.html", posts=all_posts)

if __name__ == "__main__":
    app.run(debug=True)