from flask import Blueprint, flash, redirect, render_template, url_for
from flask_login import current_user, login_user, logout_user, login_required

from learning_log_flask.extentions import db, login
from .forms import LoginForm, RegisterForm
from .modules import User


@login.user_loader
def load_user(id):
    return User.query.get(int(id))

@login.unauthorized_handler
def unathorized():
    """ Redirect unauthorized users to Login page """
    flash('Ooopsy...You must been logged in to view that page')
    return redirect(url_for('users_bp.login'))

users_bp = Blueprint('users_bp', __name__, template_folder='templates')

@users_bp.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('ll_bp.index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password. Try again')
            return redirect(url_for('users_bp.login'))
        login_user(user)
        return redirect(url_for('ll_bp.index'))
    return render_template('login.html', form=form)        

@users_bp.route('/register', methods=['GET', 'POST'])
def register():
    """ A new user registration """
    form = RegisterForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None:
            new_user = User(username=form.username.data, 
                            first_name=form.first_name.data,
                            last_name=form.last_name.data,
                            email=form.email.data)
            new_user.set_password(form.password.data)
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user)
            return redirect(url_for('ll_bp.index'))
    return render_template('register.html', form=form)

@users_bp.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('ll_bp.index'))