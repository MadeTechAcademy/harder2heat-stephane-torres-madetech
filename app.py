import json
from flask import Flask, render_template
from src.utils import get_list_of_buildings_from_os_data

app = Flask(__name__)

with open('properties.json') as json_properties:
    data = json.load(json_properties)
    properties = get_list_of_buildings_from_os_data(data)



@app.route("/")
def home():

    return render_template("home.html", properties=properties)
