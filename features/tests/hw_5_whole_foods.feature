# Created by maxmal at 3/6/22
Feature: Whole foods promo page

  Scenario: Verify that every product on the Wholefoods page has a text ‘Regular’ and a product name
    Given Open Whole Foods Promo page
    Then Verify product has a text "Regular"
    And Verify product has a product name