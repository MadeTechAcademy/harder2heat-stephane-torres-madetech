import json
from flask import Flask, render_template
from src.utils import get_properties_from_os
app = Flask(__name__)

properties = None
with open('properties.json') as json_properties:
   data = json.load(json_properties)
   properties = get_properties_from_os(data)

@app.route("/")
def home():
   return render_template("home.html", properties=properties)