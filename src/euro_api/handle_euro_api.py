import json
import requests


def get_euro_data(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
    except Exception as e:
         return {"status_code": 500, "response_body": str(e)}
