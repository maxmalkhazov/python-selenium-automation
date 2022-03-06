# Created by maxmal at 3/5/22
Feature: Tests for product page

  Scenario: User can select colors for product B082YMKNKT
    Given Open Amazon product B082YMKNKT page
    Then Verify user can click through 3 colors


  Scenario: User can select color for product B081YS2F7N
    Given Open Amazon product B081YS2F7N page
    Then Verify user can click through 5 colors