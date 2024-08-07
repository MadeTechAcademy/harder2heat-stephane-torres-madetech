from src.property import Property


class Building:

    def __init__(self, coordinates, attributes):
        self.coordinates = coordinates
        self.attributes = attributes
        self.properties = self.set_properties()


    def set_properties(self):
        for attribute in self.attributes:
            for key, value in attribute.items():
                if key == "uprnreference":
                    for property in attribute.get("uprnreference"):
                        self.properties.append(Property(property['uprn']))
