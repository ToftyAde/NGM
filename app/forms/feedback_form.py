from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Email, Length

class FeedbackForm(FlaskForm):
    name = StringField(
        'Name',
        validators=[
            DataRequired(message="Please enter your name."),
            Length(max=50, message="Name must be 50 characters or fewer.")
        ]
    )
    email = StringField(
        'Email',
        validators=[
            DataRequired(message="Please enter your email."),
            Email(message="Please enter a valid email address."),
            Length(max=120, message="Email must be 120 characters or fewer.")
        ]
    )
    message = TextAreaField(
        'Message',
        validators=[
            DataRequired(message="Please enter your feedback."),
            Length(max=500, message="Feedback must be 500 characters or fewer.")
        ]
    )
    submit = SubmitField('Send Feedback')
