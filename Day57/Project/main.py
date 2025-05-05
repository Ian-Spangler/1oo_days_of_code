# Blog Capstone Project Part 1
from flask import Flask, render_template
from post import Post

app = Flask(__name__)

post = Post()

@app.route('/')
def home():
    blogs = post.get_blogs()
    return render_template("index.html", posts=blogs)

@app.route('/post/<int:num>')
def get_post(num):
    blog = post.get_choosen_blog(num)
    return render_template("post.html", post=blog)

if __name__ == "__main__":
    app.run(debug=True)
