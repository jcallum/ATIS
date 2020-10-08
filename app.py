import json
import re

import requests
from flask import Flask, redirect, render_template
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'

class MyForm(FlaskForm):
    icao = StringField('ICAO code', validators=[DataRequired()])


def get_metar(icao):
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
    print("In get_atis", icao)
    get_metar(icao)
    return

@app.route('/', methods=('GET', 'POST'))
def submit():
    form = MyForm()
    if form.validate_on_submit():
        get_atis(form.icao)
        return redirect('/success')
    return render_template('submit.html', form=form)

@app.route('/success')
def success():
    return redirect('/display')

if __name__ == '__main__':
    app.run(debug=True)   
