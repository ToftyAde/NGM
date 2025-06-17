# run.py
from app import create_app
from app.extensions import db

# Import models so their tables get registered in metadata
from app.models.user import User  
from app.models.game import Game  

app = create_app()

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
