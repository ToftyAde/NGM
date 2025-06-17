from flask import Blueprint, render_template
from flask_login import login_required, current_user
from sqlalchemy import desc
from app.models.game import Game

user_bp = Blueprint('user', __name__)

@user_bp.route('/profile')
@login_required
def profile():
    """
    User profile page: stats and recent games.
    """
    # Aggregate stats
    total_games = Game.query.filter_by(player_id=current_user.id).count()
    wins = Game.query.filter_by(player_id=current_user.id, won=True).count()

    # Best score calculation
    best_game = (
        Game.query
            .filter_by(player_id=current_user.id, won=True)
            .order_by(desc(Game.max_attempts - Game.attempts + 1))
            .first()
    )
    best_score = best_game.score if best_game else 0

    # Recent 5 games sorted by finish time
    recent_games = (
        Game.query
            .filter_by(player_id=current_user.id)
            .order_by(desc(Game.finished_at))
            .limit(5)
            .all()
    )

    return render_template(
        'profile.html',
        total_games=total_games,
        wins=wins,
        best_score=best_score,
        recent_games=recent_games
    )
