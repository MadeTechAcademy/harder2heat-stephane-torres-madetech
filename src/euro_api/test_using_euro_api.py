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

    @patch("handle_euro_api.requests")
    def test_euro_api_responds_200(self, mock_requests):

        response = MagicMock()
        response.status_code = 200
        response.json.return_value = euro_api_mock_response
        mock_requests.get.return_value = response


        body = get_euro_data()
        self.assertEqual(body["status_code"],200)
        self.assertEqual(body["body"][0]["properties"]["number_of_floors"],2 )

    @patch("handle_euro_api.requests")
    def test_euro_api_responds_500(self, mock_requests):
        response = MagicMock()
        response.status_code = 500
        response.json.return_value = {"status_code": 500, "response_body": "Internal Server Error"}
        mock_requests.get.return_value = response
        body = get_euro_data()
        self.assertRaises(Exception, get_euro_data())
        self.assertEqual(body.args[0]["status_code"],  500)
        self.assertEqual(body.args[0]["status_code"], response.status_code)




if __name__ == "__main__":
    unittest.main()