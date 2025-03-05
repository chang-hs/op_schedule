from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, DateField, BooleanField, SubmitField
from wtforms.validators import InputRequired, Length, Optional

class OpForm(FlaskForm):
    patient_id = StringField('patient_id', validators=[InputRequired(), Length(min=8, max=8)])
    name = StringField('name', validators=[InputRequired()])
    diagnosis = StringField('diagnosis', validators=[InputRequired()])
    op_duration = StringField('op_duration')
    urgency = IntegerField('urgency')
    submit = SubmitField('Submit')

class EditOpForm(FlaskForm):
    id = StringField('id')
    patient_id = StringField('patient_id', validators=[InputRequired(), Length(min=8, max=8)])
    name = StringField('name', validators=[InputRequired()])
    diagnosis = StringField('diagnosis', validators=[InputRequired()])
    op_duration = StringField('op_duration')
    urgency = IntegerField('urgency')
    op_date = DateField('op_date', validators=[Optional()])
    preop_date = DateField('preop_date',validators=[Optional()])
    date_set = BooleanField('date_set')
    patient_notified = BooleanField('patient_notified')
    orders_committed = BooleanField('orders_committed')
    submit = SubmitField('Submit')