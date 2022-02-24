# Created by maxmal at 2/22/22
Feature: Customer Service page


  Scenario: Verify UI elements are present
    Given Open Amazon Customer Service page
    Then Verify primary header is present
    Then Verify 9 help content boxes are present
    Then Verify search help field is present
    Then Verify secondary header is present
    Then Verify 12 support help topics menu is present