import json
import unittest
from morelia import run, verify
from ..utils import get_list_of_buildings_from_os_data



class BuildingTestCases(unittest.TestCase):

    def setUp(self):
        with open("../../properties.json") as buildings_json:
            data = json.load(buildings_json)
            buildings = get_list_of_buildings_from_os_data(data)

        self.buildings = buildings


    def test_number_of_buildings(self):
        """Number of buildings feature"""
        verify("building.feature", self)
    #
    def step_The_page_loads(self):
        r"The page loads"
        # self.setUp()
        self.result = 3 + 1


    def step_number_properties_on_the_page_should_be_displayed(self, number):
        r'"{number}" properties on the page should be displayed'

        self.assertEqual(int(number), len(self.buildings))
