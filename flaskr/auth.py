import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash

from flaskr.db import get_db

bp = Blueprint('auth', __name__, url_prefix='/auth')

@bp.route('/signup', methods = ('POST', 'GET'))
def signup():
    if request.method == 'POST':
        email = request.form['email']
        username = request.form['username']
        password = request.form['password']
        flash(username)
        db = get_db()
        error = None
        if not email:
            error = 'Email is required!'
        elif not username:
            error = 'Username is required!'
        elif not password:
            error = 'Password is required!'
        elif db.execute(
            'SELECT id from users where email = ?', (email,)
        ).fetchone() is not None:
            error = 'Email {} already registered'.format(email)
        elif db.execute(
            'SELECT id from users where username = ?', (username,)
        ).fetchone() is not None:
            error = 'User {} already exists!'.format(username)

        if error is None:
            db.execute(
                'INSERT INTO users (email, username, password) VALUES (?, ?, ?)',
                (email, username, generate_password_hash(password))
            )
            db.commit()
            return render_template(url_for('auth.login'))
        flash(error)
    return render_template('auth/signup.html')    

@bp.route('/login', methods=('GET', 'POST'))
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        db = get_db()
        error = None
        user = db.execute(
            'SELECT * FROM users WHERE username = ?', (username,)
        ).fetchone()

        if user is None:
            error = 'Incorrect username.'
        elif not check_password_hash(user['password'], password):
            error = 'Incorrect password.'

        if error is None:
            session.clear()
            session['user_id'] = user['id']
            return redirect(url_for('index'))

        flash(error)

    return render_template('auth/login.html')

@bp.before_app_request
def load_logged_in_user():
    user_id = session.get('user_id')

    if user_id is None:
        g.user = None
    else:
        g.user = get_db().execute(
            'SELECT * FROM users WHERE id = ?', (user_id,)
        ).fetchone()

@bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))

def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for('auth.login'))

        return view(**kwargs)

    return wrapped_view