from src.building import Building
from src.utils import get_list_of_buildings_from_european_data

MOCK_RESPONSE_DATA = {
    "number_of_floors": 2,
    "distance_to_transport": 35
}




def test_get_building_from_euro_data_returns_buildings():
    assert isinstance(get_list_of_buildings_from_european_data(), list)
    assert isinstance(get_list_of_buildings_from_european_data()[0], Building)

def test_building_from_euro_data_has_number_of_floors():
    assert any("number_of_floors" in attribute for attribute in get_list_of_buildings_from_european_data()[0].attributes)

def test_building_from_euro_data_has_distance_to_transport():
    assert any("distance_to_transport" in attribute for attribute in get_list_of_buildings_from_european_data()[0].attributes)