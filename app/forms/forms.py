from flask_wtf import FlaskForm
from wtforms import (
    StringField,
    TextAreaField,
    SelectField,
    IntegerField,
    PasswordField,
    BooleanField,
    SubmitField
)
from wtforms.validators import (
    DataRequired,
    Email,
    Length,
    NumberRange,
    EqualTo
)


class ContactForm(FlaskForm):
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
    subject = StringField(
        'Subject',
        validators=[
            DataRequired(message="Please enter a subject."),
            Length(max=100, message="Subject must be 100 characters or fewer.")
        ]
    )
    message = TextAreaField(
        'Message',
        validators=[
            DataRequired(message="Please enter your message."),
            Length(max=500, message="Message must be 500 characters or fewer.")
        ]
    )
    submit = SubmitField('Send Message')


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
    rating = IntegerField(
        'Rating',
        validators=[
            DataRequired(message="Please select a rating."),
            NumberRange(min=1, max=5, message="Rating must be between 1 and 5.")
        ]
    )
    category = SelectField(
        'Category',
        choices=[
            ('bug', 'Bug Report'),
            ('feature', 'Feature Request'),
            ('general', 'General Feedback')
        ],
        validators=[
            DataRequired(message="Please select a category.")
        ]
    )
    feedback = TextAreaField(
        'Feedback',
        validators=[
            DataRequired(message="Please enter your feedback."),
            Length(max=500, message="Feedback must be 500 characters or fewer.")
        ]
    )
    submit = SubmitField('Submit Feedback')


class GameForm(FlaskForm):
    level = SelectField(
        'Choose Difficulty Level',
        choices=[
            ('easy', 'Easy (0–99)'),
            ('medium', 'Medium (0–999)'),
            ('expert', 'Expert (0–9 999)')
        ],
        validators=[DataRequired(message="Please select a difficulty level.")]
    )
    submit = SubmitField('Start Game')


class GuessForm(FlaskForm):
    guess = IntegerField(
        'Your Guess',
        validators=[
            DataRequired(message="Please enter a number."),
            NumberRange(min=0, message="Enter a valid number.")
        ]
    )
    submit = SubmitField('Submit')


class LoginForm(FlaskForm):
    email = StringField(
        'Email',
        validators=[
            DataRequired(message="Please enter your email."),
            Email(message="Please enter a valid email address."),
            Length(max=120, message="Email must be 120 characters or fewer.")
        ]
    )
    password = PasswordField(
        'Password',
        validators=[
            DataRequired(message="Please enter your password."),
            Length(min=6, message="Password must be at least 6 characters.")
        ]
    )
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Login')


class RegisterForm(FlaskForm):
    username = StringField(
        'Username',
        validators=[
            DataRequired(message="Please enter your username."),
            Length(min=3, max=25, message="Username must be between 3 and 25 characters.")
        ]
    )
    email = StringField(
        'Email',
        validators=[
            DataRequired(message="Please enter your email."),
            Email(message="Please enter a valid email address.")
        ]
    )
    password = PasswordField(
        'Password',
        validators=[
            DataRequired(message="Please enter your password."),
            Length(min=6, message="Password must be at least 6 characters.")
        ]
    )
    confirm_password = PasswordField(
        'Confirm Password',
        validators=[
            DataRequired(message="Please confirm your password."),
            EqualTo('password', message="Passwords must match.")
        ]
    )
    submit = SubmitField('Register')


class ForgotPasswordForm(FlaskForm):
    email = StringField(
        'Email',
        validators=[
            DataRequired(message="Please enter your email."),
            Email(message="Please enter a valid email address."),
            Length(max=120, message="Email must be 120 characters or fewer.")
        ]
    )
    submit = SubmitField('Request Password Reset')
