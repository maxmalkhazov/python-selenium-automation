# Created by maxmal at 2/13/22
Feature: Amazon Cart Tests

  Scenario: Verify that Amazon cart is empty
    Given Open Amazon homepage
    When Click on cart icon
    Then Verify cart is empty


  Scenario: Verify item was added to the cart
    Given Open Amazon homepage
    When Search for Pen
    And Click search
    And Click on item
    And Add item to cart
    Then Verify item exists in cart


  Scenario: User can see language options
    Given Open Amazon homepage
    When Hover over language options
    Then Verify Spanish option present


  Scenario Outline: User can select and search in a department
    Given Open Amazon homepage
    When Select department by alias <alias>
    And Search for Faust
    And Click search
    Then Verify <department> department is selected
    Examples:
    |alias   |department   |
    |stripbooks   |books    |
    |audible   |audible   |