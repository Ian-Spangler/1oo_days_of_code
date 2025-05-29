# Blog Capstone Project Part 4
from flask import Flask, render_template, redirect, url_for, request, flash
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy import Integer, String, Text, ForeignKey
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, URL
from flask_ckeditor import CKEditor, CKEditorField
from datetime import date
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user
from werkzeug.security import generate_password_hash, check_password_hash
from forms import AddForm, RegisterForm, LoginForm, CommentForm
from functools import wraps
from flask import abort
from flask_gravatar import Gravatar

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)

class Base(DeclarativeBase):
    pass
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////workspaces/1oo_days_of_code/Day69/Project/instance/posts.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)


class Post(db.Model):
    __tablename__ = "post"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    author_id: Mapped[int] = mapped_column(Integer, db.ForeignKey("user.id"))
    author = relationship("User", back_populates="posts")
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    subtitle: Mapped[str] = mapped_column(String(250), nullable=False)
    date: Mapped[str] = mapped_column(String(250), nullable=False)
    body: Mapped[str] = mapped_column(Text, nullable=False)
    img_url: Mapped[str] = mapped_column(String(250), nullable=False)
    comments = relationship("Comment", back_populates="parent_post")

class User(UserMixin, db.Model):
    __tablename__ = "user"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    email: Mapped[str] = mapped_column(String(100), unique=True)
    password: Mapped[str] = mapped_column(String(100))
    name: Mapped[str] = mapped_column(String(1000))
    posts = relationship("Post", back_populates="author")
    comments = relationship("Comment", back_populates="comment_author")

class Comment(db.Model):
    __tablename__ = "comment"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    author_id: Mapped[int] = mapped_column(Integer, db.ForeignKey("user.id"))
    comment_author = relationship("User", back_populates="comments")
    post_id: Mapped[int] = mapped_column(Integer, db.ForeignKey("post.id"))
    parent_post = relationship("Post", back_populates="comments")
    text: Mapped[str] = mapped_column(Text, nullable=False)

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

login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return db.get_or_404(User, user_id)

def admin_only(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        #If id is not 1 then return abort with 403 error
        if current_user.id != 1:
            return abort(403)
        #Otherwise continue with the route function
        return f(*args, **kwargs)        
    return decorated_function

@app.route('/')
def home():
    result = db.session.execute(db.select(Post))
    all_posts = result.scalars().all()
    return render_template("index.html", data=all_posts, logged_in=current_user.is_authenticated)

@app.route('/about')
def about():
    return render_template("about.html", logged_in=current_user.is_authenticated)

@app.route('/contact')
def contact():
    return render_template("contact.html", logged_in=current_user.is_authenticated)

gravatar = Gravatar(app,
                    size=100,
                    rating='g',
                    default='retro',
                    force_default=False,
                    force_lower=False,
                    use_ssl=False,
                    base_url=None)

@app.route('/post/<post_id>', methods=["GET", "POST"])
def post(post_id):
    form = CommentForm()
    post = db.get_or_404(Post, post_id)
    if form.validate_on_submit():
        if not current_user.is_authenticated:
            flash("Please log in to comment")
            return redirect(url_for('login'))
        else:
            data = request.form
            new_comment = Comment(author=current_user, text=data["comment"])
            db.session.add(new_comment)
            db.session.commit()
    return render_template("post.html", blog=post, form=form, logged_in=current_user.is_authenticated, comments=post.comments)

@app.route('/new-post', methods=["GET", "POST"])
@admin_only
def add_post():
    form = AddForm()
    if form.validate_on_submit():
        current_date = date.today().strftime("%B %d, %Y")
        data = request.form
        new_post = Post(title=data["title"], subtitle=data["subtitle"], author=current_user, img_url=data["img_url"], body=data["body"], date=current_date)
        db.session.add(new_post)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template("make-post.html", form=form, function="New Post", logged_in=current_user.is_authenticated)
    
@app.route('/edit-post/<post_id>', methods=["GET", "POST"])
@admin_only
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
    return render_template("make-post.html", form=form, function="Edit Post", logged_in=current_user.is_authenticated)

@app.route('/delete-post/<post_id>', methods=["GET", "POST"])
@admin_only
def delete_post(post_id):
    post_to_delete = db.get_or_404(Post, post_id)
    db.session.delete(post_to_delete)
    db.session.commit()
    return redirect(url_for('home'))

# TODO: Use Werkzeug to hash the user's password when creating a new user.
@app.route('/register', methods=["GET", "POST"])
def register():
    form = RegisterForm()
    if request.method == "POST":
        data = request.form
        result = db.session.execute(db.select(User).where(User.email == data["email"]))
        user = result.scalar()
        if user:
            flash("You've already signed up with that email, log in instead!")
            return redirect(url_for("login"))
        else:
            hashed_and_salted_password = generate_password_hash(password=data["password"], method="pbkdf2", salt_length=8)
            new_user = User(email=data["email"], password=hashed_and_salted_password, name=data["name"])
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user)
            return redirect(url_for("home"))
    return render_template("register.html", form=form, logged_in=current_user.is_authenticated)


# TODO: Retrieve a user from the database based on their email. 
@app.route('/login', methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        data = request.form
        result = db.session.execute(db.select(User).where(User.email == data["email"]))
        user = result.scalar()
        if not user:
            flash('The email does not exist. Please try again.')
            return redirect(url_for('login'))
        elif check_password_hash(pwhash=user.password, password=data["password"]):
            login_user(user)
            return redirect(url_for("home"))
        else:
            flash('Password incorrect. Please try again.')
            return redirect(url_for('login'))
    return render_template("login.html", form=form, logged_in=current_user.is_authenticated)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))

if __name__ == "__main__":
    app.run(debug=True)
