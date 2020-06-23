# Created by ingabukhvalova at 6/21/20
Feature: # Test scenarios for add product to cart
  # Enter feature description here

  Scenario: User can add a Product to a Cart
    Given Open a page with multiple Products
    When Click on Product image to add to Cart
    Then Verify a card is not empty


  #Create your own test case to add any product you want into the cart,
  #and make sure it’s there (check for the number
  #of items in the cart OR open the cart and verify it’s there, up to you!)