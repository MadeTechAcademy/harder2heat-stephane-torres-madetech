from enum import Enum

from src.property import Property
from src.enums import DesiredAttribrutesFromBuildingPropterties


#  TODO more refactoring, introduce .get()
#   so that we can pass an alternative if an attribute/property is not found.
def get_properties_from_os(list_of_buildings):
    list_of_properties = []
    for building in list_of_buildings:
        coordinates = building["geometry"]["coordinates"][0]
        attributes = building["properties"]
        list_of_uprns = attributes["uprnreference"]
        for individual_property in list_of_uprns:
            age = (
                "buildingage_year"
                if attributes["buildingage_year"]
                else "buildingage_period"
            )
            new_property = Property(individual_property["uprn"])
            new_property.connectivity = get_property_connectivity(attributes["connectivity"])
            new_property.age = attributes[age]
            new_property.material = attributes["constructionmaterial"]
            new_property.coordinates = coordinates
            new_property.osid = attributes.get("osid", None)
            new_property.date_age_last_updated = attributes.get("buildingage_updatedate", None)
            new_property.area_m2 = attributes.get("geometry_area_m2", "Unknown")
            list_of_properties.append(new_property)

    return list_of_properties


property_connectivities = {
    "Standalone": "Free-Standing",
    "Semi-Connected": "Dual-Connected",
    "End Connected": "Single Connected",
}

def get_property_connectivity(connectivity: str) -> str:
   return property_connectivities.get(connectivity, connectivity)

# TODO two ways to neaten this up, pull some of the logic from the factory into get_desired so factory only returns an obj and does nothing else
#   means factory doesn't need to care about enums, might make the factory more reusable
def get_desired_attributes_from_building_properties(desired_attributes: Enum, building_properties: dict) -> list[dict]:

    list_of_desired_attributes = []

    for desired_attribute in desired_attributes:
        value = building_properties.get(desired_attribute.value, None)

        if value == None:
            raise AttributeError(f'Attribute {desired_attribute} not found')

        if desired_attribute.value == DesiredAttribrutesFromBuildingPropterties.CONNECTIVITY.value:
            value = get_property_connectivity(value)

        list_of_desired_attributes.append(attribute_factory(desired_attribute.value, value))

    return list_of_desired_attributes

def attribute_factory(desired_attribute: str, value: str) -> dict:
    return {desired_attribute: value}



            
#








