from enum import Enum


class Connectivity(Enum):
    pass

class DesiredAttribrutesFromBuildingPropterties(Enum):
    OSID = "osid"
    AREA = "geometry_area_m2"
    # COORDINATES = "coordinates" TODO this is from the buildings geometry NOT properties
    AGE_LAST_UPDATED = "buildingage_updatedate"
