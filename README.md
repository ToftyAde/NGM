# Number Guessing Game (NGG)

A Flask web application where users can register, log in, and play a number guessing game with multiple difficulty levels. Features user authentication, admin panel, leaderboard, feedback, and more.

## Features
- User registration and login with secure password hashing
- Session management with Flask-Login
- Admin panel (Flask-Admin)
- Number guessing game with multiple difficulty levels
- Leaderboard and user profiles
- Feedback and contact forms
- Responsive UI with Bootstrap

## Setup Instructions

### 1. Clone the repository
```bash
git clone <repo-url>
cd <repo-directory>
```

### 2. Create and activate a virtual environment
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Set up the database
```bash
python run.py  # or flask db upgrade if using migrations
```

### 5. Run the application
```bash
python run.py
```

The app will be available at `http://127.0.0.1:5000/`.

## Admin Access
To promote a user to admin:
```bash
python manage.py make_admin <email> [--password NEW_PASSWORD]
```

## Configuration
- Set your `SECRET_KEY` and other sensitive values as environment variables or in a `.env` file for production.

## Contribution Guidelines
- Fork the repository and create a feature branch.
- Follow PEP8 and use `black` for formatting.
- Submit a pull request with a clear description of your changes.

## License
MIT License 