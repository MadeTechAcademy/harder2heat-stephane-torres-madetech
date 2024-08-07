import json
from flask import Flask, render_template
from src.utils import get_properties_from_os, get_list_of_buildings_from_os

app = Flask(__name__)

with open('properties.json') as json_properties:
    data = json.load(json_properties)
    properties = get_list_of_buildings_from_os(data)
    print(properties)


@app.route("/")
def home():
    print(properties)

    return render_template("home.html", properties=properties)
