
from flask_wtf import Form
from wtforms import StringField, PasswordField, SubmitField, TextAreaField, FloatField, SelectField
from wtforms.validators import DataRequired, Email, Length
from dbAccess import *

class SignupForm(Form):
  name = StringField('Name', validators=[DataRequired("Please enter your name.")])
  email = StringField('Email', validators=[DataRequired("Please enter your email address."), Email("Please enter your email address.")])
  password = PasswordField('Password', validators=[DataRequired("Please enter a password."), Length(min=6, message="Passwords must be 6 characters or more.")])
  loginType = SelectField('Create as', choices=(('User', 'User'), ('Manager', 'Manager')))
  submit = SubmitField('Sign up')


class LoginForm(Form):
    email = StringField('Email', validators=[DataRequired("Please enter your email address."), Email("Please enter your email address.")])
    password = PasswordField('Password', validators=[DataRequired("Please enter a password.")])
    loginType = SelectField('Login as', choices=( ('User','User'), ('Manager','Manager')))
    submit = SubmitField('Sign in')

class ItemForm(Form):
    itemname = StringField('Item Name',validators=[DataRequired("Please enter an item name.")])
    quantity = FloatField('Qunatity', validators=[DataRequired("Please enter quantity.")])
    notes = TextAreaField('Notes')
    submit = SubmitField('Add Item')

class PersonForm(Form):
    aadhar = StringField('Aadhar number',validators=[DataRequired("PLease enter aadhar")])
    name = StringField("Name", validators=[DataRequired("PLease enter a name")])
    salary = StringField("Salary", validators=[DataRequired("PLease enter a salary")])

class RemovePersonForm(Form):
    pps = getSalaryTable()
    ids = []
    for i in pps:
        ids.append((i[0],i[0]))
    ids = tuple(ids)
    print("aadhar numbers are")
    print(ids)
    removeid = SelectField('Aadhar id ', choices=ids)
    submit = SubmitField('Remove person')


class PropertyForm(Form):
    ids = getIds()
    print(ids)
    aadhar = SelectField(u'Aadhar number', validators=[DataRequired("PLease select an option")], choices=ids)
    #aadhar = StringField('Aadhar number',validators=[DataRequired("PLease enter aadhar")])
    owner = StringField("owner", validators=[DataRequired("PLease enter a owner")])
    pname = StringField("pname", validators=[DataRequired("PLease enter a property name")])
    estimatedvalue = StringField("Esti Value", validators=[DataRequired("PLease enter a value")])

class RemovePropertyForm(Form):
    pps = getPropertyTable()
    ids = []
    for i in pps:
        ids.append((i[0],i[0]))
    ids = tuple(ids)
    print("aadhar numbers are")
    print(ids)
    removeid = SelectField('Aadhar id ', choices=ids)
    submit = SubmitField('Remove property')
    
class VehicleForm(Form):
    ids = getIds()
    aadhar = SelectField(u'Aadhar number', validators=[DataRequired("PLease select an option")], choices=ids)
    owner = StringField("owner", validators=[DataRequired("PLease enter a owner")])
    vname = StringField("vname", validators=[DataRequired("PLease enter a vehicle name")])
    estimatedvalue = StringField("Esti Value", validators=[DataRequired("PLease enter a value")])


class RemoveVehicleForm(Form):
    print("#### vehicle fomrsssssssssssss")
    pps = getVehicleTable()
    ids = []
    for i in pps:
        ids.append((i[0],i[0]))
    ids = tuple(ids)
    print("aadhar numbers are")
    print(ids)
    removeid = SelectField('Aadhar id ', choices=ids)
    submit = SubmitField('Remove vehicle')


class ContactForm(Form):
  senderName = StringField("Name")
  senderEmail = StringField("Email")
  emailSubject = StringField("Subject")
  emailMessage = TextAreaField("Message")
  submit = SubmitField("Send")