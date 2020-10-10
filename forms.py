from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class InputForm(FlaskForm):
    icao = StringField('ICAO', validators=[DataRequired()])
    submit = SubmitField('Enter')

class DisplayForm(FlaskForm):
    icao = StringField('ICAO', validators=[DataRequired()])
    station_name = StringField('Station', validators=[DataRequired()])