from app import create_app
from app.extensions import db
from app.models.user import User
import click

app = create_app()

@app.cli.command("make_admin")
@click.argument("email")
@click.option("--password", default=None, help="Set a new password for the user.")
def make_admin(email, password):
    """Promote a user to admin and optionally set their password."""
    with app.app_context():
        user = User.query.filter_by(email=email).first()
        if user:
            user.is_admin = True
            if password:
                user.set_password(password)
            db.session.commit()
            click.echo(f"User {user.username} ({user.email}) is now admin! Password updated: {bool(password)}")
        else:
            click.echo("User not found.")

if __name__ == "__main__":
    app.run() 