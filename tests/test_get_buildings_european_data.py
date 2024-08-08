from src.building import Building
from src.utils import get_list_of_buildings_from_european_data


def test_get_building_from_euro_data_returns_buildings():
    assert isinstance(get_list_of_buildings_from_european_data(), list)
    assert isinstance(get_list_of_buildings_from_european_data()[0], Building)

def test_building_from_euro_data_has_windows():
    assert any("number_of_windows" in attribute for attribute in get_list_of_buildings_from_european_data()[0].attributes)