# Created by maxmal at 2/13/22
Feature: Amazon Cart

  Scenario: Verify that Amazon cart is empty
    Given Open Amazon Home page
    When Click on cart icon
    Then Verify cart is empty


  Scenario: Verify item was added to the cart
    Given Open Amazon Home page
    When Search for Pen
    And Click search
    And Click on item
    And Add item to cart
    Then Verify item exists in cart