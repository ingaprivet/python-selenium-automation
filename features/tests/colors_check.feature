# Created by ingabukhvalova at 6/24/20
Feature: Test Scenarios for loop thru available colors

  Scenario: User opens a Product page where a color selection is available
    Given Open a Product page
    When Color selection toggle group is available
    Then 8 color choices items are present
    And Loop thru available colors


