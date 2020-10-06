from flask import Flask, render_template
app = Flask(__name__)
import requests
import json

hdr = {"X-API-Key": "3c5ff1a1547644ffac404bdeba"}
req = requests.get("https://api.checkwx.com/metar/kjfk/decoded", headers=hdr)

#print("Response from CheckWX.... \n")

try:
    req.raise_for_status()
    resp = json.loads(req.text)
    #print(json.dumps(resp, indent=1))

except requests.exceptions.HTTPError as e:
    print(e)

@app.route("/")
@app.route("/atis/")
#@app.route("/atis/<icao>")
def get_atis(icao = None):
    return render_template(
        "get_atis.html",
        icao = icao
    )

@app.route("/atis/<icao>")
def display_atis(icao = None):
    global resp
    return resp

