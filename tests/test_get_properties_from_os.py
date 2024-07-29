import json
from src.utils import get_properties_from_os

with open('properties.json') as json_properties:
   data = json.load(json_properties)
   properties = get_properties_from_os(data)

EXPECTED_SAMPLE_LENGTH = len(properties)


def test_tests_are_running():
    assert True




def test_length_of_sample_properties_is_as_expected():
    assert len(properties) == EXPECTED_SAMPLE_LENGTH