import json

from src.property import Property
from src.utils import get_desired_attributes_from_building_properties
from src.enums import DesiredAttribrutesFromBuildingGeometryOS, DesiredAttributesFromBuildingPropertiesOS
from src.building import Building

with open('properties.json') as json_properties:
    data = json.load(json_properties)


test_building = Building(coordinates=get_desired_attributes_from_building_properties(DesiredAttribrutesFromBuildingGeometryOS, data[0]["geometry"]),
                         attributes=get_desired_attributes_from_building_properties(DesiredAttributesFromBuildingPropertiesOS, data[0]["properties"]))

def test_building_has_a_list_of_coordinates():
    assert isinstance(test_building.coordinates, list)
    assert test_building.coordinates == [{"coordinates": data[0]["geometry"]["coordinates"]}]

def test_building_has_a_list_of_desired_attributes():
    assert isinstance(test_building.attributes, list)
    assert test_building.attributes[0] == {"osid": data[0]["properties"]["osid"]}

def test_building_has_a_list_of_properties():
    assert isinstance(test_building.properties, list)
    assert isinstance(test_building.properties[0], Property)
