from src.property import Property


class Building:

    def __init__(self, coordinates, attributes):
        self.coordinates = coordinates
        self.attributes = attributes
        self.properties: list[Property] = []


