from src.property import Property


#  TODO more refactoring, introduce .get()
#   so that we can pass an alternative if an attribute/property is not found.
def get_properties_from_os(list_of_buildings):
    list_of_properties = []
    for building in list_of_buildings:
        coordinates = building["geometry"]["coordinates"][0][0]
        properties = building["properties"]
        list_of_uprns = properties["uprnreference"]
        for individual_property in list_of_uprns:
            age = (
                "buildingage_year"
                if properties["buildingage_year"]
                else "buildingage_period"
            )
            new_property = Property(individual_property["uprn"])
            new_property.connectivity = properties["connectivity"]
            new_property.age = properties[age]
            new_property.material = properties["constructionmaterial"]
            new_property.long = coordinates[0]
            new_property.lat = coordinates[1]
            list_of_properties.append(new_property)

    return list_of_properties

            









