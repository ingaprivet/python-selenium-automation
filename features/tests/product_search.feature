# Created by Svetlana
Feature: Test Scenarios for Search functionality

  Scenario: User can search for an item in any Amazon department
    Given Open Amazon page
    When Select mi department
    And Search for Piano
    Then Musical Instruments department in selected
    Then Product results for Piano are shown

  #Scenario: User can search for a product
    #Given Open Amazon page
    #When Search for Dress
    #Then Product results for Dress are shown


  #Scenario: User can select Books department
    #Given Open Amazon page
    #When Select stripbooks department
    #And Search for Faust
    #Then Books department in selected




