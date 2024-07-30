from src.property import Property
from area import area


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
            new_property.age_last_updated = properties.get("buildingage_updatedate", None)
            list_of_properties.append(new_property)

    return list_of_properties


property_connectivities = {
    "Standalone": "Free-Standing",
    "Semi-Connected": "Dual-Connected",
    "End Connected": "Single Connected",
}

def get_property_connectivity(connectivity: str) -> str:
   return property_connectivities.get(connectivity, "Unknown")

def get_property_area(property) -> float:
    return area(property)


            









