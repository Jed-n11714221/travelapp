from flask_wtf import FlaskForm
from wtforms.fields import TextAreaField,SubmitField, StringField, PasswordField
from wtforms.validators import InputRequired, Email, EqualTo, Length
from flask_wtf.file import FileRequired, FileField, FileAllowed

ALLOWED_FILE = {'PNG','JPG','png','jpg'}

class DestinationForm(FlaskForm):
  name = StringField('Country', validators=[InputRequired()])
  # adding two validators, one to ensure input is entered and other to check if the 
  # description meets the length requirements
  description = TextAreaField('Description', validators = [InputRequired()])
  image = FileField('Destination Image', validators=[
    FileRequired(message = 'Image cannot be empty'),
    FileAllowed(ALLOWED_FILE, message='Only supports png, jpg, JPG, PNG')])
  currency = StringField('Currency', validators=[InputRequired()])
  submit = SubmitField("Create")

class LoginForm(FlaskForm):
    user_name = StringField("User Name", validators=[InputRequired('Enter user name')])
    password = PasswordField("Password", validators=[InputRequired('Enter user password')])
    submit = SubmitField("Login")

class RegisterForm(FlaskForm):
    user_name = StringField("User Name", validators=[InputRequired()])
    email_id = StringField("Email Address", validators=[Email("Please enter a valid email")])
    
    password = PasswordField("Password", validators=[InputRequired(),
                  Length(min=8, message="Password must be at least 8 characters long"),
                  EqualTo('confirm', message="Passwords should match")])
    confirm = PasswordField("Confirm Password")
    submit = SubmitField("Register")

class CommentForm(FlaskForm):
  text = TextAreaField('Comment', [InputRequired()])
  submit = SubmitField('Create')