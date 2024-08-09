import json
import requests


def get_euro_data():
    try:
        response = requests.get("http://euro-api.com")
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception ({"status_code": 500, "response_body": "Internal Server Error"})
    except Exception as e:
        return e.args


