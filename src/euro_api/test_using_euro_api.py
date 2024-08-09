import unittest

from unittest.mock import patch, MagicMock
from handle_euro_api import get_euro_data

euro_api_mock_response = {
    "status_code": 200,
    "body": [{
        "geometry": {"coordinates": [[[1,2], [3,4], [5,6]]]},
        "properties": {"number_of_floors": 2,
                       "distance_from_transport": 35,
                       "geometry_area_m2": 12,
                       "buildingage_updatedate":"2020-12-25",
                       "connectivity": "End-Connected",
                       "osid":123456}
    }]
}

class TestEuroAPI(unittest.TestCase):

    def setUp(self):
        self.url = "http://euro-api.com"

    @patch("handle_euro_api.requests")
    def test_euro_api_responds_200(self, mock_requests):

        response = MagicMock()
        response.status_code = 200
        response.json.return_value = euro_api_mock_response
        mock_requests.get.return_value = response


        body = get_euro_data(self.url)
        self.assertEqual(body["status_code"],200)


if __name__ == "__main__":
    unittest.main()