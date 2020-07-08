# Created by ingabukhvalova
Feature: Window handling

  Scenario: Company's website is open in a new tab
    Given Open a company's Yelp page
    When Click on a website link
    And Switch to a new window
    Then The Anchors fish & chips and sea food grill website is open
    And A user can close the new window and go to the original one
