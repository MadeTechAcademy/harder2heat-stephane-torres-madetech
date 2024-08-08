import json
from enum import Enum
import pytest
from src.building import Building
from src.enums import DesiredAttributesFromBuildingPropertiesOS
from src.utils import get_property_connectivity, get_desired_attributes_from_building_attributes, \
    get_list_of_buildings_from_os_data

with open('properties.json') as json_properties:
    data = json.load(json_properties)
    buildings = get_list_of_buildings_from_os_data(data)

EXPECTED_SAMPLE_LENGTH = 4
MOCK_FIRST_PROPERTY = {
    "coordinates": data[0]["geometry"]["coordinates"][0],
    "osid": data[0]["properties"]["osid"],
    "age_last_updated": data[0]["properties"]["buildingage_updatedate"],
    "connectivity": "Dual-Connected",
    "area": data[0]["properties"]["geometry_area_m2"]
}

FIRST_BUILDING = buildings[0]


def test_tests_are_running():
    assert True


def test_length_of_sample_properties_is_as_expected():
    assert len(buildings) == EXPECTED_SAMPLE_LENGTH


def test_type_of_properties_is_a_list():
    assert isinstance(buildings, list)

def test_type_object_in_properties_is_a_building():
    assert isinstance(buildings[0], Building)

def test_building_has_list_of_coordinates():
    for attribute in FIRST_BUILDING.attributes:
        if "coordinate" in attribute.keys():
            assert True
            assert attribute.value() == MOCK_FIRST_PROPERTY["coordinates"]

def test_building_has_OSID():
    assert any("osid" in attribute for attribute in FIRST_BUILDING.attributes)
    # for attribute in FIRST_BUILDING.attributes:
    #     if "osid" in attribute.keys():
    #         assert True
    #         assert attribute["osid"] == MOCK_FIRST_PROPERTY["osid"]


def test_building_has_age_last_updated_attribute():
    for attribute in FIRST_BUILDING.attributes:
        if "buildingage_updatedate" in attribute.keys():
            assert True
            assert attribute["buildingage_updatedate"] == MOCK_FIRST_PROPERTY["age_last_updated"]


def test_building_has_connectivity_attribute():
    for attribute in FIRST_BUILDING.attributes:
        if "connectivity" in attribute.keys():
            assert True
            assert attribute["connectivity"] == MOCK_FIRST_PROPERTY["connectivity"]

def test_building_has_area_attribute():
    for attribute in FIRST_BUILDING.attributes:
        if "geometry_area_m2" in attribute.keys():
            assert True
            assert attribute["geometry_area_m2"] == MOCK_FIRST_PROPERTY["area"]

#
def test_get_property_connectivity():
    assert get_property_connectivity("Semi-Connected") == "Dual-Connected"
    assert get_property_connectivity("Standalone") == "Free-Standing"
    assert get_property_connectivity("End Connected") == "Single Connected"


def test_get_desired_attributes_from_building_properties_returns_dicts_of_desired_attributes():
    expected = [{"osid": MOCK_FIRST_PROPERTY["osid"]}, {"geometry_area_m2": MOCK_FIRST_PROPERTY["area"]},
                {"buildingage_updatedate": MOCK_FIRST_PROPERTY["age_last_updated"]},
                {"connectivity": MOCK_FIRST_PROPERTY["connectivity"]},
                {'uprnreference': [{'buildingid': '02ae4ae4-6119-4d72-aef9-e56013d25e0d', 'buildingversiondate': '2024-05-25', 'uprn': 100090062842}]}
]
    assert get_desired_attributes_from_building_attributes(DesiredAttributesFromBuildingPropertiesOS, data[0]["properties"]) == expected

def test_error_is_thrown_when_attribute_not_found():
    class WrongAttributes(Enum):
        AREA = "area"

    with pytest.raises(AttributeError):
        get_desired_attributes_from_building_attributes(WrongAttributes, data[0]["properties"])



