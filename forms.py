from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, DateField, BooleanField, SubmitField
from wtforms.validators import InputRequired, Length, Optional

class OpForm(FlaskForm):
    patient_id = StringField('patient_id', validators=[InputRequired(), Length(min=8, max=8)])
    name = StringField('name', validators=[InputRequired()])
    age = IntegerField('age', validators=[Optional()])
    diagnosis = StringField('diagnosis', validators=[InputRequired()])
    op_duration = StringField('op_duration')
    urgency = IntegerField('urgency')
    memo = StringField('memo')
    phone = StringField('phone')
    email = StringField('email')
    submit = SubmitField('Submit')

class EditOpForm(FlaskForm):
    id = StringField('id')
    patient_id = StringField('patient_id', validators=[InputRequired(), Length(min=8, max=8)])
    name = StringField('name', validators=[InputRequired()])
    age = IntegerField('age', validators=[Optional()])
    diagnosis = StringField('diagnosis', validators=[InputRequired()])
    op_duration = StringField('op_duration')
    urgency = IntegerField('urgency')
    memo = StringField('memo')
    op_date = DateField('op_date', validators=[Optional()])
    preop_date = DateField('preop_date',validators=[Optional()])
    date_set = BooleanField('date_set')
    patient_notified = BooleanField('patient_notified')
    orders_committed = BooleanField('orders_committed')
    submit = SubmitField('Submit')

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired(), Length(min=4, max=20)])
    password = PasswordField('Password', validators=[InputRequired(), Length(min=6, max=20)])
    submit = SubmitField('Login')