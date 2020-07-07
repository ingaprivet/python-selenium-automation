# Created by ingabukhvalova at 6/5/20
Feature: Logged out user sees Sign in page when clicking Orders

  Scenario: Verify search for Cancel Order
    Given Open Amazon page
    When Click Orders
    Then Verify Sign-In page is opened

