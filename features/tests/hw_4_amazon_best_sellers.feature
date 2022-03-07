# Created by maxmal at 2/20/22
Feature: Amazon Best Sellers page

  Scenario: Verify there are 5 links
    Given Open Amazon Best Sellers page
    Then Verify there are 5 links
    Then Click on each link and verify correct page opens
