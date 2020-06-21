# Created by ingabukhvalova at 6/13/20

Feature: Test for cart functionality
  # Enter feature description here

  Scenario: User verifies that his Shopping Cart is empty
    # Enter steps here
  Given Open Amazon page
  When Click on Cart Icon
    Then Verify the Shopping Cart is empty
