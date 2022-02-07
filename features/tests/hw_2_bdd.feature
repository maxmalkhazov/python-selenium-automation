# Created by maxmal at 2/6/22
Feature: Amazon test case


  Scenario: Logged out user sees Sign in page when clicking Orders
    Given Open Amazon page
    When Click Orders
    Then Verify Sign in page opened
