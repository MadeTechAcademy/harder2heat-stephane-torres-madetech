import json
from src.utils import get_properties_from_os


def test_tests_are_running():
    assert True


with open('properties.json') as json_properties:
   data = json.load(json_properties)
   properties = get_properties_from_os(data)

def test_length_of_sample_properties_is_four():
    assert len(properties) == 4