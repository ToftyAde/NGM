import random
from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user
from app.forms.forms import GameForm, GuessForm
from app.models.game import Game
from app.extensions import db

game_bp = Blueprint('game', __name__, url_prefix='/game')

@game_bp.route('/start', methods=['GET', 'POST'])
@login_required
def start_game():
    """
    Display and process the new game form.
    """
    form = GameForm()
    if form.validate_on_submit():
        level = form.level.data
        # Define ranges & max attempts per level
        config = {
            'easy':   {'range': (0, 99),   'max_attempts': 10},
            'medium': {'range': (0, 999),  'max_attempts': 10},
            'expert': {'range': (0, 9999), 'max_attempts': 10},
        }[level]

        low, high = config['range']
        secret = random.randint(low, high)

        # Create a new Game, using 'target' not 'secret_number'
        game = Game(
            player_id=current_user.id,
            level=level,
            target=secret,
            attempts=0,
            max_attempts=config['max_attempts']
        )
        db.session.add(game)
        db.session.commit()
        return redirect(url_for('game.play', game_id=game.id))

    return render_template('game/start.html', form=form)


@game_bp.route('/play/<int:game_id>', methods=['GET', 'POST'])
@login_required
def play(game_id):
    """
    Show the game play screen and handle guess submissions.
    """
    form = GuessForm()
    game = Game.query.get_or_404(game_id)
    message = None

    if form.validate_on_submit():
        guess = form.guess.data
        game.attempts += 1

        if guess == game.target:
            game.won = True
            game.finished_at = datetime.utcnow()
            db.session.commit()
            flash('🎉 Congratulations! You guessed correctly.', 'success')
            return redirect(url_for('game.result', game_id=game.id))

        if game.attempts >= game.max_attempts:
            game.won = False
            game.finished_at = datetime.utcnow()
            db.session.commit()
            flash('💥 Game Over! You have used all attempts.', 'danger')
            return redirect(url_for('game.result', game_id=game.id))

        message = 'Too low!' if guess < game.target else 'Too high!'
        db.session.commit()

    return render_template(
        'game/play.html',
        form=form,
        game=game,
        message=message
    )


@game_bp.route('/result/<int:game_id>')
@login_required
def result(game_id):
    """
    Display the result of a completed game.
    """
    game = Game.query.get_or_404(game_id)
    return render_template('game/result.html', game=game)
