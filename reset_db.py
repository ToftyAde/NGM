# reset_db.py
from app import create_app
from app.extensions import db

app = create_app()
with app.app_context():
    # WARNING: this will **delete** all your existing data
    db.drop_all()
    db.create_all()
    print("Database schema reset. All tables recreated.")
