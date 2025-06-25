import os
from flask import Flask
from app.extensions import db, login_manager, migrate
from app.admin import init_admin


def create_app():
    # Determine project root (one level above app/)
    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

    # Initialize Flask app with custom static and template folders
    app = Flask(
        __name__,
        static_folder=os.path.join(project_root, 'static'),
        static_url_path='/static',
        template_folder=os.path.join(os.path.dirname(__file__), 'templates')
    )
    app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'dev_secret_key')  # Set SECRET_KEY in environment for production

    # SQLite database path in project_root/database/app.db
    db_path = os.path.join(project_root, 'database', 'app.db')
    app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{db_path}"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'
    
    # Admin setup
    init_admin(app)

    # User loader callback for Flask-Login
    from app.models.user import User

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    # Register blueprints
    from app.routes.auth_routes import auth_bp
    from app.routes.game_routes import game_bp
    from app.routes.user_routes import user_bp
    from app.routes.main_routes import main_bp

    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(game_bp, url_prefix='/game')
    app.register_blueprint(user_bp, url_prefix='/user')
    app.register_blueprint(main_bp)

    return app