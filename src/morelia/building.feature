Feature: Displays correct building information
  In order to ascertain how many building there are in a given area
  As a user
  I want to see the number of buildings displayed on the page

Background: When the user visits the page
  And The page loads

Scenario: Display correct number of buildings
  Then "4" properties on the page should be displayed

Scenario: Each building should have an OSID
  Then There should be "4" osid displayed