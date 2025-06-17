import random
from datetime import datetime
from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_required, current_user
from sqlalchemy import desc

from app.extensions import db
from app.models.game import Game
from app.forms.game_form import GameForm
from app.forms.guess_form import GuessForm

# Blueprint for game routes
game_bp = Blueprint('game', __name__, template_folder='templates/game')

@game_bp.route('/start', methods=['GET', 'POST'])
@login_required
def start_game():
    """
    Start a new guessing game by selecting a level.
    """
    form = GameForm()
    if form.validate_on_submit():
        level = form.level.data
        # determine target range
        ranges = {'Low': 100, 'Moderate': 1000, 'Expert': 10000}
        target_range = ranges.get(level, 100)
        target = random.randint(0, target_range - 1)

        # Create and save new game using player_id
        game = Game(
            player_id=current_user.id,
            level=level,
            target=target,
            attempts=0,
            max_attempts=10,
            won=False,
            finished_at=None
        )
        db.session.add(game)
        db.session.commit()
        return redirect(url_for('game.play_game', game_id=game.id))

    return render_template('game/start.html', form=form)

@game_bp.route('/play/<int:game_id>', methods=['GET', 'POST'])
@login_required
def play_game(game_id):
    """
    Play the guessing game: submit guesses and receive hints.
    """
    form = GuessForm()
    # Filter by player_id instead of user_id
    game = Game.query.filter_by(id=game_id, player_id=current_user.id).first_or_404()

    if form.validate_on_submit():
        guess = form.guess.data
        game.attempts += 1

        if guess == game.target:
            game.won = True
            game.finished_at = datetime.utcnow()
            db.session.commit()
            flash(f"🎉 Correct! You guessed it in {game.attempts} attempts.", "success")
            return redirect(url_for('game.results', game_id=game.id))

        if game.attempts >= game.max_attempts:
            game.finished_at = datetime.utcnow()
            db.session.commit()
            flash(f"❌ Out of attempts! The number was {game.target}.", "danger")
            return redirect(url_for('game.results', game_id=game.id))

        hint = 'Too low!' if guess < game.target else 'Too high!'
        attempts_left = game.max_attempts - game.attempts
        flash(f"{hint} Attempts left: {attempts_left}", "info")
        db.session.commit()
        return redirect(url_for('game.play_game', game_id=game.id))

    return render_template('game/play.html', game=game, form=form)

@game_bp.route('/results/<int:game_id>')
@login_required
def results(game_id):
    """
    Show the game results, including score and target number.
    """
    game = Game.query.filter_by(id=game_id, player_id=current_user.id).first_or_404()
    return render_template('game/results.html', game=game)
