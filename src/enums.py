from enum import Enum


class DesiredAttributesFromBuildingAttributesOS(Enum):
    OSID = "osid"
    AREA = "geometry_area_m2"
    AGE_LAST_UPDATED = "buildingage_updatedate"
    CONNECTIVITY = "connectivity"

class DesiredAttribrutesFromBuildingGeometryOS(Enum):
    COORDINATES = "coordinates"


class DesiredAttribrutesFromBuildingAttributesEuro(Enum):
    NUMBER_OF_FLOORS = "number_of_floors"
    DISTANCE_TO_TRANSPORT = "distance_to_transport"
