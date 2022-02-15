# Created by maxmal at 2/13/22
Feature: Search the help library

  Scenario: User can search for page by text
    Given Open Amazon Help page
    When User inputs text in search field
    Then User is redirected to matching page