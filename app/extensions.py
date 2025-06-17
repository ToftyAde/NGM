from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_migrate import Migrate

# Initialize extensions
# SQLAlchemy for ORM
# Bcrypt for password hashing
# LoginManager for user session management
# Migrate for database migrations

db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()
migrate = Migrate()

# Flask-Login settings
login_manager.login_view = 'auth.login'
login_manager.login_message_category = 'info'
