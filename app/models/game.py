# app/models/game.py

from datetime import datetime
from app.extensions import db
from app.models.user import User

class Game(db.Model):
    __tablename__ = 'games'

    id = db.Column(db.Integer, primary_key=True)
    player_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    player = db.relationship('User', backref=db.backref('games', lazy=True))

    level = db.Column(db.String(20), nullable=False)
    target = db.Column(db.Integer, nullable=False)      # secret number to guess
    attempts = db.Column(db.Integer, default=0, nullable=False)
    max_attempts = db.Column(db.Integer, nullable=False)
    score = db.Column(db.Integer, default=0, nullable=False)
    won = db.Column(db.Boolean, default=False, nullable=False)
    started_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    finished_at = db.Column(db.DateTime, nullable=True)  # when the game ends

    def __repr__(self):
        return (
            f"<Game id={self.id} "
            f"player={self.player.username} "
            f"level={self.level} "
            f"target={self.target} "
            f"attempts={self.attempts}/{self.max_attempts} "
            f"won={self.won}>"
        )
