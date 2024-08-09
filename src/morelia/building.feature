Feature: Displays correct building information
  As a user I would like to know certain characteristics of buildings and how many there are.
  I want to see the number of buildings
  I want to see their OSIDs
  I want to see their area in metres squared
  I want to see their connectivity
  I would like to know when the age of the building was last updated


Background: When the user visits the page
  And The page loads

Scenario: Display correct number of buildings
  Then "4" properties on the page should be displayed

Scenario: Each building should have an OSID
  Then There should be "4" osid displayed

Scenario: Each building should have an area
  Then There should be "4" areas displayed

Scenario: Each building should show its connectivity
  Then There should be "4" connectivities displayed