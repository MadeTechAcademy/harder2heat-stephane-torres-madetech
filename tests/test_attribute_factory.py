import json
import pytest
from src.utils import attribute_factory


with open('properties.json') as json_properties:
    data = json.load(json_properties)
    buildings_attributes: list = []
    for building in data:
        buildings_attributes.append(building.get("properties"))


def test_attribute_factory_returns_dict():
    assert isinstance(attribute_factory("osid", buildings_attributes[0]), dict)

def test_attribute_factory_returns_desired_attribute_osid():
    assert attribute_factory("osid", buildings_attributes[0]["osid"]) == {"osid": buildings_attributes[0]["osid"]}


