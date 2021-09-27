from flask import Blueprint, url_for, render_template, flash, request, session
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import redirect

bp = Blueprint('main', __name__, url_prefix='/')

from project.forms import UserLoginForm
from project.models import User

@bp.route('/')
def index():
    return redirect(url_for('main.login')) # main.login으로 변경

@bp.route('/login/', methods=('GET', 'POST'))
def login():
    form = UserLoginForm()
    error = None

    if request.method == 'POST' and form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        password = User.query.filter_by(password=form.password.data).first()
        
        if not user:
            error = "존재하지 않는 사용자입니다."
        # elif not check_password_hash(user.password, form.password.data):
        elif not password:
            error = "비밀번호가 올바르지 않습니다."
        
        if error is None:
            session.clear()
            session['user_id'] = user.id
            return redirect(url_for('main.camera'))
        flash(error)
    return render_template('login.html', form=form, e=error)

@bp.route('/camera/')
def camera():
    return render_template('change_video.html')
