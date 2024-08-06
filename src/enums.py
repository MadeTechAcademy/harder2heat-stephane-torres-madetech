from enum import Enum


class Connectivity(Enum):
    pass

class DesiredAttribrutesFromBuildingPropterties(Enum):
    OSID = "osid"
    AREA = "geometry_area_m2"
    # COORDINATES = "coordinates" TODO this is from the buildings geometry NOT properties
    AGE_LAST_UPDATED = "buildingage_updatedate"
    CONNECTIVITY = "connectivity"
#     TODO can an enum have a dict as it's value? thinking for connectivity, or do
#       or do we create connectivity enums so that we can...
#       or have I looped the wrong way around?
