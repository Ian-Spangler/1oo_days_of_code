from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length

'''
Red underlines? Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''

class MyForm(FlaskForm):
    email = StringField(label='Email', validators=[DataRequired(), Email(message="Invalid email address")])
    password = PasswordField(label='Password', validators=[DataRequired(), Length(min=8, message="Field must be at least 8 characters long.")])
    submit = SubmitField(label='Log In')

app = Flask(__name__)

app.secret_key = "some secret string"

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/login", methods=["GET", "POST"])
def login():
    form = MyForm()
    if form.validate_on_submit():
        if form.email.data == "asdf@gmail.com" and form.password.data == "12345678":
            return render_template('success.html', form=form)
        else:
            return render_template('denied.html', form=form)
    else:
        return render_template('login.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
