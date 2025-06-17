from flask_wtf import FlaskForm
from wtforms import SelectField, SubmitField
from wtforms.validators import DataRequired

class GameForm(FlaskForm):
    level = SelectField(
        'Choose Difficulty Level',
        choices=[('Low', 'Low (0–99)'), ('Moderate', 'Moderate (0–999)'), ('Expert', 'Expert (0–9999)')],
        validators=[DataRequired(message="Please select a difficulty level.")]
    )
    submit = SubmitField('Start Game')
