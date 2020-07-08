# Created by Svetlana
Feature: Test Scenarios for Search functionality

  Scenario: User can search for a product
    Given Open Amazon page
    When Search for Dress
    Then Product results for Dress are shown