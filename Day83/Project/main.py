# Portfolio Web App

from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap5 import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Text
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, URL
from flask_ckeditor import CKEditor, CKEditorField
from datetime import date
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'YOUR_SECRET_KEY'
Bootstrap(app)
CKEditor(app)

# DB CONFIG
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{os.path.join(basedir, 'instance', 'projects.db')}"

class Base(DeclarativeBase):
    pass

db = SQLAlchemy(model_class=Base)
db.init_app(app)

# ---------------- MODEL ----------------
class Project(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    short_description: Mapped[str] = mapped_column(String(250), nullable=False)
    date: Mapped[str] = mapped_column(String(250), nullable=False)
    project_detail: Mapped[str] = mapped_column(Text, nullable=False)
    author: Mapped[str] = mapped_column(String(250), nullable=False)
    img_url: Mapped[str] = mapped_column(String(500), nullable=False)
    github_url: Mapped[str] = mapped_column(String(500), nullable=True)
    demo_url: Mapped[str] = mapped_column(String(500), nullable=True)

with app.app_context():
    db.create_all()

# -------------- FORM --------------------
class ProjectForm(FlaskForm):
    title = StringField('Project Title', validators=[DataRequired()])
    short_description = StringField('Short Description', validators=[DataRequired()])
    author = StringField('Developer Name', validators=[DataRequired()])
    img_url = StringField('Feature Image URL', validators=[URL()])
    github_url = StringField('GitHub Repository URL', validators=[URL()])
    demo_url = StringField('Live Demo URL', validators=[URL()])
    project_detail = CKEditorField('Project Details (Features, Tech Stack)', validators=[DataRequired()])
    submit = SubmitField('SAVE PROJECT')

# ---------------- ROUTES ----------------

@app.route('/')
def home():
    result = db.session.execute(db.select(Project))
    all_projects = result.scalars().all()
    return render_template("index.html", projects=all_projects)

@app.route('/project/<project_id>')
def show_project(project_id):
    project = db.get_or_404(Project, project_id)
    return render_template("project.html", project=project)

@app.route('/new', methods=["GET", "POST"])
def add_project():
    form = ProjectForm()
    if form.validate_on_submit():
        current_date = date.today().strftime("%B %d, %Y")
        new_project = Project(
            title=form.title.data,
            short_description=form.short_description.data,
            img_url=form.img_url.data,
            github_url=form.github_url.data,
            project_detail=form.project_detail.data,
            date=current_date
        )
        db.session.add(new_project)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template("make-project.html", form=form, function="New Project")

@app.route('/edit/<project_id>', methods=["GET", "POST"])
def edit_project(project_id):
    project_to_update = db.get_or_404(Project, project_id)
    form = ProjectForm(
        title=project_to_update.title,
        short_description=project_to_update.short_description,
        img_url=project_to_update.img_url,
        github_url=project_to_update.github_url,
        demo_url=project_to_update.demo_url,
        author=project_to_update.author,
        project_detail=project_to_update.project_detail
    )
    if form.validate_on_submit():
        project_to_update.title = form.title.data
        project_to_update.short_description = form.short_description.data
        project_to_update.img_url = form.img_url.data
        project_to_update.github_url = form.github_url.data
        project_to_update.demo_url = form.demo_url.data
        project_to_update.author = form.author.data
        project_to_update.project_detail = form.project_detail.data
        db.session.commit()
        return redirect(url_for('show_project', project_id=project_id))
    return render_template("make-project.html", form=form, function="Edit Project")

@app.route('/delete/<project_id>')
def delete_project(project_id):
    project_to_delete = db.get_or_404(Project, project_id)
    db.session.delete(project_to_delete)
    db.session.commit()
    return redirect(url_for('home'))

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/contact')
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True)
