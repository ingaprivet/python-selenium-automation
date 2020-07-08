# Created by i bukhvalova
Feature: Amazon main page popup

  Scenario: Sign in popup appears and then disappers
    Given Open Amazon page
    Then Verify Sign in popup is present and clickable
    When Sign in popup disappears
    Then Verify Sign in popup is not clickable