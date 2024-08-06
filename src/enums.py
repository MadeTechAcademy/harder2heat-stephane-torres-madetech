from enum import Enum


class Connectivity(Enum):
    pass

class DesiredAttribrutesFromBuildingPropterties(Enum):
    OSID = "osid"
    AREA = "geometry_area_m2"
    AGE_LAST_UPDATED = "buildingage_updatedate"
    CONNECTIVITY = "connectivity"

class DesiredAttribrutesFromBuildingGeometry(Enum):
    COORDINATES = "coordinates"
