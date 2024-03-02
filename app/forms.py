from typing import Text
from flask_wtf import FlaskForm
from wtforms import TextAreaField, StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Length

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')


class PostForm(FlaskForm):
    title = StringField('Title', validators=[
        DataRequired(), Length(min=1, max=120)])
    ingredients = TextAreaField('Ingredients', validators=[
        DataRequired(), Length(min=3, max=2000)])
    instructions = TextAreaField('Instructions', validators=[
        DataRequired(), Length(min=3, max=2000)])
    tags = StringField('Tags', validators=[
        DataRequired(), Length(min=3, max=500)])
    submit = SubmitField('Submit')





    
