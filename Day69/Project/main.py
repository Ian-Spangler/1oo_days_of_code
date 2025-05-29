# Blog Capstone Project Part 4
from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Text
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, URL
from flask_ckeditor import CKEditor, CKEditorField
from datetime import date


app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)

class Base(DeclarativeBase):
    pass
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////workspaces/1oo_days_of_code/Day67/Project/instance/posts.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)


class Post(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    subtitle: Mapped[str] = mapped_column(String(250), nullable=False)
    date: Mapped[str] = mapped_column(String(250), nullable=False)
    body: Mapped[str] = mapped_column(Text, nullable=False)
    author: Mapped[str] = mapped_column(String(250), nullable=False)
    img_url: Mapped[str] = mapped_column(String(250), nullable=False)

def to_dict(self):
    return {
        "id": self.id,
        "title": self.title,
        "date": self.date,
        "body": self.body,
        "author": self.author,
        "img_url": self.img_url,
        "subtitle": self.subtitle
    }

with app.app_context():
    db.create_all()

class AddForm(FlaskForm):
    title = StringField('Blog Post Title', validators=[DataRequired()])
    subtitle = StringField('Subtitle', validators=[DataRequired()])
    author = StringField('Your Name', validators=[DataRequired()])
    img_url = StringField('Blog Image URL', validators=[DataRequired()])
    body = CKEditorField('Blog Content', validators=[DataRequired()])
    submit = SubmitField('SUBMIT POST')

@app.route('/')
def home():
    result = db.session.execute(db.select(Post))
    all_posts = result.scalars().all()
    return render_template("index.html", data=all_posts)

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/contact')
def contact():
    return render_template("contact.html")

@app.route('/post/<post_id>')
def post(post_id):
    post = db.get_or_404(Post, post_id)
    return render_template("post.html", blog=post)

@app.route('/new-post', methods=["GET", "POST"])
def add_post():
    form = AddForm()
    if form.validate_on_submit():
        current_date = date.today().strftime("%B %d, %Y")
        data = request.form
        new_post = Post(title=data["title"], subtitle=data["subtitle"], author=data["author"], img_url=data["img_url"], body=data["body"], date=current_date)
        db.session.add(new_post)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template("make-post.html", form=form, function="New Post")
    
@app.route('//edit-post/<post_id>', methods=["GET", "POST"])
def edit_post(post_id):
    post_to_update = db.get_or_404(Post, post_id)
    form = AddForm(
        title=post_to_update.title,
        subtitle=post_to_update.subtitle,
        img_url=post_to_update.img_url,
        author=post_to_update.author,
        body=post_to_update.body
    )
    if form.validate_on_submit():
        data = request.form
        post_to_update.title = data["title"]
        post_to_update.subtitle = data["subtitle"]
        post_to_update.img_url = data["img_url"]
        post_to_update.author = data["author"]
        post_to_update.body = data["body"]
        db.session.commit()
        return redirect(url_for('post', post_id=post_id))
    return render_template("make-post.html", form=form, function="Edit Post")

@app.route('//delete-post/<post_id>', methods=["GET", "POST"])
def delete_post(post_id):
    post_to_delete = db.get_or_404(Post, post_id)
    db.session.delete(post_to_delete)
    db.session.commit()
    return redirect(url_for('home'))

# TODO: Use Werkzeug to hash the user's password when creating a new user.
@app.route('/register')
def register():
    return render_template("register.html")


# TODO: Retrieve a user from the database based on their email. 
@app.route('/login')
def login():
    return render_template("login.html")


@app.route('/logout')
def logout():
    return redirect(url_for('get_all_posts'))

if __name__ == "__main__":
    app.run(debug=True)
