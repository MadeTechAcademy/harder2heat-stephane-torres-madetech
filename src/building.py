from src.property import Property


class Building:

    def __init__(self, coordinates, attributes):
        self.coordinates = coordinates
        self.attributes = attributes
        self.properties: list[Property] = []
        self.get_properties_from_attributes()


    def get_properties_from_attributes(self):
        for attribute in self.attributes:
            for key, value in attribute.items():
                if key == "uprnreference":
                    for property in attribute.get("uprnreference"):
                        self.properties.append(Property(property['uprn']))

        # return self.properties
# THIS IS STINKY