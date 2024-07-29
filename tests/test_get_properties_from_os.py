import json

from src.property import Property
from src.utils import get_properties_from_os

with open('properties.json') as json_properties:
    data = json.load(json_properties)
    properties = get_properties_from_os(data)

EXPECTED_SAMPLE_LENGTH = 4
MOCK_FIRST_PROPERTY_COORDINATES = data[0]["geometry"]["coordinates"][0]
MOCK_FIRST_PROPERTY_OSID = data[0]["properties"]["osid"]


def test_tests_are_running():
    assert True


def test_length_of_sample_properties_is_as_expected():
    assert len(properties) == EXPECTED_SAMPLE_LENGTH

def test_type_of_properties_is_a_list():
    assert isinstance(properties, list)

def test_type_object_in_properties_is_a_property():
    assert isinstance(properties[0], Property)


def test_property_has_list_of_coordinate():
    first_property = properties[0]
    assert isinstance(first_property.coordinates, list)
    assert first_property.coordinates == MOCK_FIRST_PROPERTY_COORDINATES

def test_property_has_OSID():
    first_property = properties[0]
    assert isinstance(first_property.osid, str)
    assert first_property.osid == MOCK_FIRST_PROPERTY_OSID

def test_property_has_age_last_updated_attribute():
    first_property = properties[0]
    assert isinstance(first_property.last_updated_attribute, str)
