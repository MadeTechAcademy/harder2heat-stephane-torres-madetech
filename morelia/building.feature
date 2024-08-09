#Feature: Coordinates
#  In order to know where a building is located
#  As a user
#  I want to see a list of the buildings coordinates
#
#  Scenario: Display building coordinates
#    Given I have loaded the app/homepage

Feature: Number of buildings
  In order to ascertain how many building there are in a given area
  As a user
  I want to see the number of buildings displayed on the page

Scenario: Display correct number of buildings
  Given I open the app
  When The app/page loads
  Then I should see the number of properties on the page