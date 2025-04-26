Feature: Login functionality on Sailor website

  Background:
    Given I am on the login page

  Scenario: Login with valid credential
    When I enter valid email and password
    And I click the login button
    Then I should be redirected to the account page

  Scenario: Login with invalid credential
    When I enter invalid email and password
    And I click the login button
    Then I should see an error message

  Scenario: Login with empty fields
    When I click the login button without entering credentials
    Then I should see an error message

