from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class InputForm(FlaskForm):
    icao = StringField('ICAO:      ', validators=[DataRequired()])
    submit = SubmitField('Enter')

class DisplayForm(FlaskForm):
    icao = StringField('ICAO:         ', validators=[DataRequired()])
    station_name = StringField('Station:   ', validators=[DataRequired()])
    raw_metar = StringField('METAR:', validators=[DataRequired()])
    time_zulu = StringField('Zulu Time:   ', validators=[DataRequired()])
    wind_dir = StringField('Wind: ', validators=[DataRequired()])
    wind_spd = StringField('Wind Speed', validators=[DataRequired()])
    wind_gusts = StringField('Gusts:', validators=[DataRequired()])