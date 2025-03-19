import locale
from flask import Flask, redirect, url_for
from flask_bootstrap import Bootstrap5
from flask import render_template
from models import Op, User
from forms import OpForm, EditOpForm, LoginForm
from db import db_session
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///op_schedule.db'
app.config['SECRET_KEY'] = 'hansoo77jp'

bootstrap = Bootstrap5(app)

# Set locale (change "fr_FR" to your desired locale, e.g., "de_DE" for German)
locale.setlocale(locale.LC_TIME, "ja_JP.UTF-8")

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

def set_user_password(username, password):
    new_user = User(username=username, password=generate_password_hash(password))
    db_session.add(new_user)
    db_session.commit()

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and check_password_hash(user.password, form.password.data):
            login_user(user)
            return redirect(url_for('list_ops'))
        else:
            flash('Invalid username or password', 'danger')
    return render_template('login.html', form=form)


@app.route('/')
def index():
    return 'Hello, world!'

@app.route('/register', methods=['GET', 'POST'])
@login_required
def register():
    form = OpForm()
    if form.validate_on_submit():
        new_op = Op(patient_id=form.patient_id.data, name=form.name.data, age=form.age.data, diagnosis=form.diagnosis.data,
                    memo=form.memo.data, op_duration=form.op_duration.data, urgency=form.urgency.data,
                    phone=form.phone.data, email=form.email.data)
        db_session.add(new_op)
        db_session.commit()
        return redirect(url_for('register'))
    return render_template('register.html', form=form)


@app.route('/list')
@login_required
def list_ops():
    ops = Op.query.all()
    return render_template('list_op.html', title="List of Ops", ops=ops)

@app.route('/edit/<int:op_id>', methods=['GET', 'POST'])
@login_required
def edit_op(op_id):
    op = db_session.query(Op).filter_by(id=op_id).first()
    form = EditOpForm(obj=op)
    if form.validate_on_submit():
        op.patient_id = form.patient_id.data
        op.name = form.name.data
        op.diagnosis = form.diagnosis.data
        op.urgency = form.urgency.data
        op.memo = form.memo.data
        op.op_date = form.op_date.data
        op.preop_date = form.preop_date.data
        op.date_set = form.date_set.data
        op.patient_notified = form.patient_notified.data
        op.orders_committed = form.orders_committed.data
        
        db_session.commit()
        return redirect(url_for('list_ops'))
    return render_template('edit_op.html', form=form)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True, port=5500)
