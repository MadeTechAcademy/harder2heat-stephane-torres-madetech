from src.property import Property
from src.enums import DesiredAttribrutesFromBuildingPropterties


#  TODO more refactoring, introduce .get()
#   so that we can pass an alternative if an attribute/property is not found.
def get_properties_from_os(list_of_buildings):
    list_of_properties = []
    for building in list_of_buildings:
        coordinates = building["geometry"]["coordinates"][0]
        properties = building["properties"]
        list_of_uprns = properties["uprnreference"]
        for individual_property in list_of_uprns:
            age = (
                "buildingage_year"
                if properties["buildingage_year"]
                else "buildingage_period"
            )
            new_property = Property(individual_property["uprn"])
            new_property.connectivity = get_property_connectivity(properties["connectivity"])
            new_property.age = properties[age]
            new_property.material = properties["constructionmaterial"]
            new_property.coordinates = coordinates
            new_property.osid = properties.get("osid", None)
            new_property.date_age_last_updated = properties.get("buildingage_updatedate", None)
            new_property.area_m2 = properties.get("geometry_area_m2", "Unknown")
            list_of_properties.append(new_property)

    return list_of_properties


property_connectivities = {
    "Standalone": "Free-Standing",
    "Semi-Connected": "Dual-Connected",
    "End Connected": "Single Connected",
}

def get_property_connectivity(connectivity: str) -> str:
   return property_connectivities.get(connectivity, "Unknown")


def get_desired_attributes_from_building_properties(building_properties) -> list[dict]:

    list_of_desired_attributes = []
    for desired_attribute in DesiredAttribrutesFromBuildingPropterties:
        list_of_desired_attributes.append(attribute_factory(desired_attribute.value, building_properties))

    return list_of_desired_attributes

def attribute_factory(desired_attribute: str, building_properties: dict) -> dict:
    value = building_properties.get(desired_attribute, None)
    if value == None:
        raise AttributeError(f'Attribute {desired_attribute} not found')

    if desired_attribute == DesiredAttribrutesFromBuildingPropterties.CONNECTIVITY.value:
        value = get_property_connectivity(value)
    return {desired_attribute: value}



            









