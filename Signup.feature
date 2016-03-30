# Created by Mohamed_86 at 3/27/2016
Feature: As an executive, I want users to be able to sign up,
         so that the system can save necessary to identify and verify individual user.

  Scenario: Signup test (BlueGarden)
    Given  User's name, email and password.
    When   the user's name, email and password are valid.
    Then   The system successfully registers the user.
