from flask import Flask, render_template
from forms import MyForm
import requests
import json
import re

app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'



hdr = {"X-API-Key": "3c5ff1a1547644ffac404bdeba"}
req = requests.get("https://api.checkwx.com/metar/kjfk/decoded", headers=hdr)

#print("Response from CheckWX.... \n")

try:
    req.raise_for_status()
    resp = json.loads(req.text)
    print(json.dumps(resp, indent=1))

except requests.exceptions.HTTPError as e:
    print(e)

@app.route("/")
def home():
    return render_template("get_atis.html")


@app.route("/<icao>", methods=('GET', 'POST'))
def get_atis(icao):
    print(icao)
    form = MyForm()
    if form.is_submitted:
        print("Validated")
        return render_template(
         "get_atis.html",
         icao = icao)
    return render_template("get_atis.html")


