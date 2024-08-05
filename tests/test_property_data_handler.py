from src.property_data_handler import property_data_handler


def test_property_data_handler_returns_list_of_Property_from_response_dict():
    assert isinstance(property_data_handler({}), list)

