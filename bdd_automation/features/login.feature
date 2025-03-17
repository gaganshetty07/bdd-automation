Feature: User Login on Magento

  Scenario: Successful login
    Given I am on the Magento login page
    When I enter valid login credentials
    And I submit the login form
    Then I should be logged in successfully

  Scenario: Login with incorrect credentials
    Given I am on the Magento login page
    When I enter invalid login credentials
    And I submit the login form
    Then I should see an error message

  Scenario: Login with blank credentials
    Given I am on the Magento login page
    When I leave the login fields empty
    And I submit the login form
    Then I should see a validation message
