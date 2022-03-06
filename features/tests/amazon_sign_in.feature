# Created by maxmal at 3/5/22
Feature: Amazon Sign in tests

  Scenario: Sign in page can be opened from SignIn popup
    Given Open Amazon homepage
    When Click on button from SignIn popup
    Then Verify Sign in page is opened