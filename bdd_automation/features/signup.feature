Feature: User Registration on Magento

  Scenario: Successful account creation
    Given I am on the Magento registration page
    When I enter valid registration details
    And I submit the registration form
    Then I should see a success message

  Scenario: Sign-up with an existing email
    Given I am on the Magento registration page
    When I enter an already registered email
    And I submit the registration form
    Then I should see an error message
