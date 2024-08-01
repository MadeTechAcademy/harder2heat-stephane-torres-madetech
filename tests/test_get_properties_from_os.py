import json
from src.property import Property
from src.utils import get_properties_from_os, get_property_connectivity, get_property_area

with open('properties.json') as json_properties:
    data = json.load(json_properties)
    properties = get_properties_from_os(data)

EXPECTED_SAMPLE_LENGTH = 4
MOCK_FIRST_PROPERTY = {
    "coordinates": data[0]["geometry"]["coordinates"][0],
    "osid": data[0]["properties"]["osid"],
    "age_last_updated": data[0]["properties"]["buildingage_updatedate"],
    "connectivity": "Dual-Connected",
    "area": 111.44
}

FIRST_PROPERTY = properties[0]


def test_tests_are_running():
    assert True


def test_length_of_sample_properties_is_as_expected():
    assert len(properties) == EXPECTED_SAMPLE_LENGTH

def test_type_of_properties_is_a_list():
    assert isinstance(properties, list)

def test_type_object_in_properties_is_a_property():
    assert isinstance(properties[0], Property)


def test_property_has_list_of_coordinate():
    assert isinstance(FIRST_PROPERTY.coordinates, list)
    assert FIRST_PROPERTY.coordinates == MOCK_FIRST_PROPERTY["coordinates"]

def test_property_has_OSID():
    assert isinstance(FIRST_PROPERTY.osid, str)
    assert FIRST_PROPERTY.osid == MOCK_FIRST_PROPERTY["osid"]

def test_property_has_age_last_updated_attribute():
    assert isinstance(FIRST_PROPERTY.age_last_updated, str)
    assert FIRST_PROPERTY.age_last_updated == MOCK_FIRST_PROPERTY["age_last_updated"]

def test_property_has_connectivity_attribute():
    assert isinstance(FIRST_PROPERTY.connectivity, str)
    assert FIRST_PROPERTY.connectivity == MOCK_FIRST_PROPERTY["connectivity"]

# TODO there is no case for multi-connected properties for example terraced houses or flats...
def test_get_property_connectivity():
    assert get_property_connectivity("Semi-Connected") == "Dual-Connected"
    assert get_property_connectivity("Standalone") == "Free-Standing"
    assert get_property_connectivity("End Connected") == "Single Connected"

def test_get_first_property_area():
    actual = get_property_area(FIRST_PROPERTY.coordinates)
    assert actual == MOCK_FIRST_PROPERTY["area"]

def test_property_has_area_attribute():
    assert isinstance(FIRST_PROPERTY.area, int)

