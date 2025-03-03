from flask import Flask, redirect, url_for
from flask_bootstrap import Bootstrap5
from flask import render_template
from models import Op
from models import db
from forms import OpForm


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///op_schedule.db'
app.config['SECRET_KEY'] = 'hansoo77jp'

db.init_app(app)

@app.route('/')
def index():
    return 'Hello, world!'

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = OpForm()
    if form.validate_on_submit():
        this_id = form.patient_id
        new_op = Op(patient_id=form.patient_id, name=form.name,
                    op_duration=form.op_duration, urgency=form.urgency)
        db.session.add(new_op)
        db.session.commit()
        return redirect(url_for('register'))
    return render_template('register.html', form=form)

@app.route('/list')
def list_ops():
    ops = db.session.execute(db.select(Op)).scalars()
    return render_template('list_op.html', title="List of Ops", ops=ops)

if __name__ == '__main__':
    app.run(debug=True)
