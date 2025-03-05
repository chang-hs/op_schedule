from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import InputRequired, Length

class OpForm(FlaskForm):
    patient_id = StringField('patient_id', validators=[InputRequired(), Length(min=8, max=8)])
    name = StringField('name', validators=[InputRequired()])
    diagnosis = StringField('diagnosis', validators=[InputRequired()])
    op_duration = StringField('op_duration')
    urgency = IntegerField('urgency')
    submit = SubmitField('Submit')