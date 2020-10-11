import json
import re

import requests
from flask import Flask, redirect, render_template
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired
from forms import InputForm, DisplayForm

app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'

global resp

def get_metar(icao):
    global resp
    code = icao.data
    hdr = {"X-API-Key": "3c5ff1a1547644ffac404bdeba"}
    req = requests.get("https://api.checkwx.com/metar/" + code + "/decoded", headers=hdr)

    #print("Response from CheckWX.... \n")

    try:
        req.raise_for_status()
        resp = json.loads(req.text)
        print(json.dumps(resp, indent=1))

    except requests.exceptions.HTTPError as e:
        print(e)

    return resp



def get_atis(icao):
    global resp
    print("In get_atis", icao)
    resp = get_metar(icao)
    return resp

@app.route('/', methods=('GET', 'POST'))
def submit():
    global resp
    form = InputForm()
    if form.validate_on_submit():
        resp = get_atis(form.icao)
        return redirect('/success',)
    return render_template('submit.html', form=form)

@app.route('/success')
def success():
    global resp
    form = DisplayForm()
    metar = resp.get('data')
    metar = metar[0]
    form.icao.data = metar['icao']
    form.station_name.data = metar['station']['name']
    form.raw_metar.data = metar['raw_text']
    form.time_zulu.data = metar['observed']
    form.wind_dir.data = metar['wind']['degrees']
    form.wind_spd.data = metar['wind']['speed_kts']
    form.wind_gusts.data = metar['wind']['gust_kts']

    #print(form.icao.data)
    return render_template('atis.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)   
