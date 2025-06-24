from flask import Blueprint, render_template
from flask_login import login_required, current_user
from sqlalchemy import desc, func
from app.models.game import Game

user_bp = Blueprint('user_routes', __name__)

@user_bp.route('/profile')
@login_required
def profile():
    """
    User profile page: stats, achievements, and recent games.
    """
    # Aggregate stats
    total_games = Game.query.filter_by(player_id=current_user.id).count()
    wins = Game.query.filter_by(player_id=current_user.id, won=True).count()

    # Best score (highest performance) calculation
    best_game = (
        Game.query
            .filter_by(player_id=current_user.id, won=True)
            .order_by(desc(Game.max_attempts - Game.attempts + 1))
            .first()
    )
    best_score = best_game.attempts if best_game else None

    # Average attempts across all completed games
    total_attempts = (
        Game.query
            .with_entities(func.sum(Game.attempts))
            .filter_by(player_id=current_user.id)
            .scalar() or 0
    )
    average_attempts = (
        round(total_attempts / total_games, 2)
        if total_games > 0 else None
    )

    # Recent 5 games sorted by finish time
    recent_games = (
        Game.query
            .filter_by(player_id=current_user.id)
            .order_by(desc(Game.finished_at))
            .limit(5)
            .all()
    )

    # Build achievements list
    achievements = []
    if total_games >= 1:
        achievements.append({
            'emoji': '🎯',
            'title': 'First Game',
            'description': 'You played your first game!'
        })
    if wins >= 1:
        achievements.append({
            'emoji': '🏆',
            'title': 'First Victory',
            'description': 'You won your first game!'
        })
    if best_score is not None and best_score <= 3:
        achievements.append({
            'emoji': '⚡',
            'title': 'Speedster',
            'description': f'Guessed in {best_score} attempts!'
        })

    return render_template(
        'profile.html',
        games_played=total_games,
        wins=wins,
        best_score=best_score,
        average_attempts=average_attempts,
        achievements=achievements,
        recent_games=recent_games
    )
