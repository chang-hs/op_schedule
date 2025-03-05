from flask import Flask, redirect, url_for
from flask_bootstrap import Bootstrap5
from flask import render_template
from models import Op
from forms import OpForm, EditOpForm
from db import db_session


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///op_schedule.db'
app.config['SECRET_KEY'] = 'hansoo77jp'

bootstrap = Bootstrap5(app)


@app.route('/')
def index():
    return 'Hello, world!'

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = OpForm()
    if form.validate_on_submit():
        new_op = Op(patient_id=form.patient_id.data, name=form.name.data, diagnosis=form.diagnosis.data,
                    op_duration=form.op_duration.data, urgency=form.urgency.data)
        db_session.add(new_op)
        db_session.commit()
        return redirect(url_for('register'))
    return render_template('register.html', form=form)

@app.route('/list')
def list_ops():
    ops = Op.query.all()
    return render_template('list_op.html', title="List of Ops", ops=ops)

@app.route('/edit/<int:op_id>', methods=['GET', 'POST'])
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


if __name__ == '__main__':
    app.run(debug=True)
