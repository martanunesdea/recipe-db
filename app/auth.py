import functools
from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

from .user import user_validate, user_register, user_authenticate, user_login, user_get_user_by_id

bp = Blueprint('auth', __name__, url_prefix='/auth')

@bp.route('/register', methods=('GET', 'POST'))
def register():
    if request.method == 'POST':
        error = user_validate(request.form)

        if error is None:
            user_register(request.form)
            return redirect(url_for('auth.login'))
        else:
            error = 'Details are incorrect.'
            flash(error)
            
    return render_template('auth/register.html')

@bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))
    
@bp.route('/login', methods=('GET', 'POST'))
def login():
    if request.method == 'POST':
        user = user_authenticate(request.form)

        if user:
            user_login(user)
            return redirect(url_for('index'))
        else:
            error = 'Something went wrong'
            flash(error)  

    return render_template('auth/login.html')

@bp.before_app_request
def load_logged_in_user():
    user_id = session.get('user_id')

    if user_id is None:
        g.user = None
    else:
        g.user = user_get_user_by_id(user_id)
        if g.user is False:
            print("Warning: User ID is None!")

def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for('auth.login'))

        return view(**kwargs)

    return wrapped_view
