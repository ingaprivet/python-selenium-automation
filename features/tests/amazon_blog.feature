# Created by ingabukhvalova at 6/30/20
Feature: # Test case for a new window handling

 Scenario: User can open and close Amazon Blog
    Given Open Amazon page
    When Store original windows
    And Click on blog link “See daily updates at blog.aboutamazon.com”
    And Switch to the newly opened window
    Then Amazon Blog is opened
    And User can open and close Blog menu

