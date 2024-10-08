from enum import Enum
from src.building import Building
from src.enums import DesiredAttributesFromBuildingAttributesOS, DesiredAttribrutesFromBuildingGeometryOS
from src.property import Property

property_connectivities = {
    "Standalone": "Free-Standing",
    "Semi-Connected": "Dual-Connected",
    "End Connected": "Single Connected",
}

def get_property_connectivity(connectivity: str) -> str:
   return property_connectivities.get(connectivity, connectivity)

def get_desired_attributes_from_building_attributes(desired_attributes: Enum, building_attributes: dict) -> list[dict]:

    list_of_desired_attributes = []

    for desired_attribute in desired_attributes:
        value = building_attributes.get(desired_attribute.value, None)

        if value == None:
            raise AttributeError(f'Attribute {desired_attribute.value} not found')

        if desired_attribute == DesiredAttributesFromBuildingAttributesOS.CONNECTIVITY:
            value = get_property_connectivity(value)

        list_of_desired_attributes.append(attribute_factory(desired_attribute, value))

    return list_of_desired_attributes

def attribute_factory(desired_attribute: Enum, value: str) -> dict:
    return {desired_attribute: value}


def get_list_of_buildings_from_os_data(os_buildings_data: dict) -> list[Building]:
    list_of_buildings = []
    for building in os_buildings_data:
        list_of_buildings.append(Building(coordinates=get_desired_attributes_from_building_attributes(DesiredAttribrutesFromBuildingGeometryOS, building["geometry"]),
                                          attributes=get_desired_attributes_from_building_attributes(DesiredAttributesFromBuildingAttributesOS, building["properties"])))

    for building in list_of_buildings:
        get_properties_using_uprn(building)

    return list_of_buildings


def get_properties_using_uprn(building: Building):
    for attribute in building.attributes:
        for key, value in attribute.items():
            if key == "uprnreference":
                for property in attribute.get("uprnreference"):
                    building.properties.append(Property(property['uprn']))


def get_list_of_buildings_from_european_data() -> list[Building]:
    return [Building(coordinates=[], attributes=[{"number_of_floors": 0}, {"distance_to_transport": 0}])]


            
#








