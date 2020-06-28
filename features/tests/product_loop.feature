# Created by ingabukhvalova at 6/27/20
Feature: # Enter feature name here
  # Enter feature description here

    Scenario: User open a wholefoodsdeals page and loops thru the products
    Given Open wholefoodsdeals page
    When Needed section of the page is available
    Then Verify every item has ‘Regular’ displayed
