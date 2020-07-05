# Created by ingabukhvalova at 6/18/20
Feature: Test Scenarios for BestSellers page

  Scenario: User can open BestSeller page and see 5 links
    Given Open amazon BestSellers page
    Then 5 bestsellers menu items are present
    And  Verify each top link opens a new page





