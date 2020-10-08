from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class MyForm(FlaskForm):
    icao = StringField('ICAO', validators=[DataRequired()])
    station_name = StringField('Station', validators=[DataRequired()])
    submit = SubmitField('Enter')
