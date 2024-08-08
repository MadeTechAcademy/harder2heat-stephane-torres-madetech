from enum import Enum
from src.building import Building
from src.enums import DesiredAttributesFromBuildingPropertiesOS, DesiredAttribrutesFromBuildingGeometryOS

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
            raise AttributeError(f'Attribute {desired_attribute} not found')

        if desired_attribute.value == DesiredAttributesFromBuildingPropertiesOS.CONNECTIVITY.value:
            value = get_property_connectivity(value)

        list_of_desired_attributes.append(attribute_factory(desired_attribute.value, value))

    return list_of_desired_attributes

def attribute_factory(desired_attribute: str, value: str) -> dict:
    return {desired_attribute: value}


def get_list_of_buildings_from_os_data(os_buildings_data: dict) -> list[Building]:
    list_of_buildings = []
    for building in os_buildings_data:
        list_of_buildings.append(Building(coordinates=get_desired_attributes_from_building_attributes(DesiredAttribrutesFromBuildingGeometryOS, building["geometry"]),
                                          attributes=get_desired_attributes_from_building_attributes(DesiredAttributesFromBuildingPropertiesOS, building["properties"])))

    return list_of_buildings


def get_list_of_buildings_from_european_data() -> list[Building]:
    return [Building(coordinates=[], attributes=[{"number_of_floors": 0}, {"distance_to_transport": 0}])]


            
#








