import unittest
from morelia import verify

class BuildingTestCases(unittest.TestCase):

    def test_number_of_buildings(self):
        """Number of buildings feature"""
        verify("building.feature", self)