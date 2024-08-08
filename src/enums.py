from enum import Enum


class DesiredAttributesFromBuildingPropertiesOS(Enum):
    OSID = "osid"
    AREA = "geometry_area_m2"
    AGE_LAST_UPDATED = "buildingage_updatedate"
    CONNECTIVITY = "connectivity"
    UPRNS = "uprnreference"

class DesiredAttribrutesFromBuildingGeometryOS(Enum):
    COORDINATES = "coordinates"
