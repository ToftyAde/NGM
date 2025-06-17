from flask_wtf import FlaskForm
from wtforms import IntegerField, SubmitField
from wtforms.validators import DataRequired, NumberRange

class GuessForm(FlaskForm):
    guess = IntegerField('Your Guess', validators=[DataRequired()])
    submit = SubmitField('Submit')
