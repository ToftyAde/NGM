# app/admin.py
from flask_admin import Admin, AdminIndexView
from flask_admin.contrib.sqla import ModelView
from flask_login import current_user
from flask import redirect, url_for, request
from app.models.user import User
from app.models.feedback import Feedback  # if you have one
from app.extensions import db

class SecureAdminIndexView(AdminIndexView):
    def is_accessible(self):
        return current_user.is_authenticated and current_user.is_admin

    def inaccessible_callback(self, name, **kwargs):
        return redirect(url_for('auth.login', next=request.url))

class SecureModelView(ModelView):
    def is_accessible(self):
        return current_user.is_authenticated and current_user.is_admin

    def inaccessible_callback(self, name, **kwargs):
        return redirect(url_for('auth.login', next=request.url))

def init_admin(app):
    admin = Admin(
        app,
        name='Admin Panel',
        template_mode='bootstrap4',
        index_view=SecureAdminIndexView()
    )
    admin.add_view(SecureModelView(User, db.session))
    # admin.add_view(SecureModelView(Feedback, db.session))  # if you have other models
