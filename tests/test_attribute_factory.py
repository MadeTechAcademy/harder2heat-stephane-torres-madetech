import json
from src.attribute_factory import attribute_factory


with open('../properties.json') as json_properties:
    data = json.load(json_properties)
    buildings_attributes: list = []
    for building in data:
        buildings_attributes.append(building.get("properties"))


def test_attribute_factory_returns_dict():
    assert isinstance(attribute_factory(), dict)

def test_attibute_factory_returns_desired_attribtue_osid():
    assert attribute_factory("osid") == {"osid": }