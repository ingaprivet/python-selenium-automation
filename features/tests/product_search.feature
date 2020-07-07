# Created by Svetlana at 4/4/19
Feature: Test Scenarios for Search functionality

  Scenario: User can search for a product
    Given Open Amazon page
    When Search for Dress
    Then Product results for Dress are shown