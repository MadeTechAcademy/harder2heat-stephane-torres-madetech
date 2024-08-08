from src.utils import get_list_of_buildings_from_european_data


def test_get_building_from_euro_data_returns_buildings():
    assert isinstance(get_list_of_buildings_from_european_data(), list)