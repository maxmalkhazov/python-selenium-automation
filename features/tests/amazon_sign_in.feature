# Created by maxmal at 3/5/22
Feature: Amazon Sign in tests

  Scenario: Sign in page can be opened from SignIn popup
    Given Open Amazon homepage
    When Click on button from SignIn popup
    Then Verify Sign in page is opened


  Scenario: User sees SignIn popup for a few seconds
    Given Open Amazon homepage
    Then Verify that SignIn popup shown
    Then Verify that SignIn btn is clickable
    When Wait for 6 seconds
    Then Verify that SignIn popup shown
    Then Verify that Signin popup disappears