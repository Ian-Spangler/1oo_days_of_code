# Blog Capstone Project Part 2
from flask import Flask, render_template
import requests

app = Flask(__name__)

response = requests.get(url="https://api.npoint.io/2e056593cce3ecc73ccf")
blog_data = response.json()

@app.route('/')
def home():
    return render_template("index.html", data=blog_data)

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/contact')
def contact():
    return render_template("contact.html")

@app.route('/post/<int:num>')
def post(num):
    return render_template("post.html", data=blog_data, num=num)

if __name__ == "__main__":
    app.run(debug=True)
