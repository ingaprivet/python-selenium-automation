# Created by ingabukhvalova at 6/18/20
Feature: Test Scenarios for BestSellers page

  Scenario: User can open BestSeller page and see
    Given Open amazon BestSellers page
    When Verify Zeitgeist menu is displayed
    Then Verify 5 links
