from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, TextAreaField, SubmitField, RadioField, SelectField
from wtforms import validators, ValidationError, EmailField

class ContactForm(FlaskForm):
   name = StringField("Name Of Student", [validators.DataRequired()])
   gender = RadioField('Gender', [validators.DataRequired()], choices = [('M', 'Male'), ('F', 'Female')])
   address = TextAreaField("Address", [validators.DataRequired()])
   email = StringField("Email", [validators.DataRequired(), validators.Email('Please enter the valid email address')])
   age = IntegerField("Age", [validators.DataRequired(), validators.NumberRange(min=18, message="Age must be greater than 18")])
   language = SelectField('Language', [validators.DataRequired()], choices = [('cpp', 'C++'), ('py', 'Python')])
   submit = SubmitField("Submit")