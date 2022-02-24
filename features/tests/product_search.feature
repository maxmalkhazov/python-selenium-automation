# Created by Svetlana at 4/4/19
Feature: Test Scenarios for Search functionality

  Scenario Outline: User can search for a product
    Given Open Google page
    When Input <search_word> into search field
    And Click on search icon
    Then Product results for <expected_result> are shown
    Examples:
    |search_word      |expected_result    |
    |coffee           |coffee             |
    |pen              |pen                |
    |shirt            |shirt              |
