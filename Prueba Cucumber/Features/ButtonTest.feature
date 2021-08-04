# Created by Jeferson Bettin at 3/08/2021
Feature: Search button test

  Scenario: Test button on page
    Given I am on page Choucair Home
    When I press the employs button
    Then I should be on the page of employs


    Scenario: Test of the page choucair employs
      Given I am on page choucair employs
      When I verify that the page enters correctly
      And That the information posted corresponds
      And I press the button to go to job portal
      Then I should see an exit alert box from the employs page