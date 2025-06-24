from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import login_required, current_user
from sqlalchemy import desc
from app.models.game import Game
from app.forms.forms import ContactForm, FeedbackForm  # import from consolidated forms module

main_bp = Blueprint('main', __name__)

@main_bp.context_processor
def inject_current_user():
    # Make current_user available in all templates
    return dict(current_user=current_user)

@main_bp.route('/')
def home():
    """
    Home page: welcome message and link to start a new game.
    """
    return render_template('home.html')

@main_bp.route('/leaderboard')
@login_required
def leaderboard():
    """
    Leaderboard: show top 10 completed games by score.
    """
    top_games = (
        Game.query
            .filter_by(won=True)
            .order_by(desc(Game.max_attempts - Game.attempts + 1))
            .limit(10)
            .all()
    )
    return render_template('leaderboard.html', games=top_games)

@main_bp.route('/contact', methods=['GET', 'POST'])
def contact():
    """
    Contact page: display and process the contact form.
    """
    form = ContactForm()
    if form.validate_on_submit():
        # TODO: handle form data (e.g., send email or save to DB)
        flash('Your message has been sent!', 'success')
        return redirect(url_for('main.feedback'))
    return render_template('contact.html', form=form)

@main_bp.route('/feedback', methods=['GET', 'POST'])
def feedback():
    form = FeedbackForm()

    if form.validate_on_submit():
        flash("Thank you for your feedback!", "success")
        return redirect(url_for('main.feedback'))

    return render_template('feedback.html', form=form)
