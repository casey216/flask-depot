from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Email, Length


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(max=100)])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=8)])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Login')


class PersonForm(FlaskForm):
    firstname = StringField('First Name', validators=[DataRequired(), Length(max=100)])
    lastname = StringField('Last Name', validators=[DataRequired(), Length(max=100)])
    email = StringField('Email', validators=[DataRequired(), Email(), Length(max=100)])
    phone = StringField('Phone Number', validators=[DataRequired(), Length(max=100)])


class UserForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(max=100)])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=8)])


class CustomerForm(FlaskForm):
    pass


class VendorForm(FlaskForm):
    pass


class DriverForm(FlaskForm):
    pass


class UserRegisterForm(PersonForm, UserForm):
    submit = SubmitField('Register')


class CustomerRegisterForm(PersonForm, CustomerForm):
    pass


class VendorRegisterForm(PersonForm, VendorForm):
    pass


class DriverRegisterForm(PersonForm, DriverForm):
    pass


