from flask import Flask
from flask import template_rendered
import requests
import json

app = Flask(__name__)


@app.route("/")
def mars():
    r = requests.get("https://api.nasa.gov/mars-photos/api/v1/rovers/Perseverance/latest_photos?api_key=DEMO_KEY")
    jsondata = json.loads(r.text)
    photos = jsondata['latest_photos']
    return template_rendered('index.html')

app.run(debug=True)
