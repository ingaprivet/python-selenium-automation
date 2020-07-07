# Created by lanalev at 10/13/19
Feature: Tests for hamburger menu functionality

  Scenario: Amazon Music has 6 menu items
    Given Open Amazon page
    When Click on hamburger menu
    And Click on Amazon Music menu item
    Then 6 menu items are present

