import json
import unittest
from morelia import run, verify
from ..utils import get_list_of_buildings_from_os_data, get_property_connectivity



class BuildingTestCases(unittest.TestCase):

    def setUp(self):
        with open("../../properties.json") as buildings_json:
            data = json.load(buildings_json)
            buildings = get_list_of_buildings_from_os_data(data)

        self.buildings = buildings


    def test_buildings_building_attributes(self):
        """Displays correct building information"""
        verify("building.feature", self)

    def step_The_page_loads(self):
        r'The page loads'
        self.setUp()

    def step_number_properties_on_the_page_should_be_displayed(self, number):
        r'"{number}" properties on the page should be displayed'

        self.assertEqual(int(number), len(self.buildings))

    def step_There_should_be_number_osid_displayed(self, number):
        r'There should be "{number}" osid displayed'

        osids = []
        for building in self.buildings:
            for attribute in building.attributes:
                for key, value in attribute.items():
                    if key == "osid":
                        osids.append(value)

        self.assertEqual(len(osids), int(number))

    def step_There_should_be_number_areas_displayed(self, number):
        r'There should be "{number}" areas displayed'

        areas = []
        for building in self.buildings:
            for attribute in building.attributes:
                for key, value in attribute.items():
                    if key == "geometry_area_m2":
                        areas.append(value)

        self.assertEqual(len(areas), int(number))

    def step_There_should_be_number_connectivities_displayed(self, number):
        r'There should be "{number}" connectivities displayed'

        connectivies = []
        for building in self.buildings:
            for attribute in building.attributes:
                for key, value in attribute.items():
                    if key == "connectivity":
                        connectivies.append(value)

        self.assertEqual(len(connectivies), int(number))

class ConnectivityTestCases(unittest.TestCase):

    def test_connectivity(self):
        """Differing connectivities"""
        verify("connectivity.feature", self)

    def step_a_building_has_old_connectivity(self, old_connectivity):
        r'a building has {old_connectivity}'
        self.connectivity = old_connectivity



    def step_it_should_read_new_connectivity(self, new_connectivity):
        r'it should read {new_connectivity}'
        self.assertEqual(get_property_connectivity(self.connectivity), new_connectivity)
