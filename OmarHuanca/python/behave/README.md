# Research

- When and why BDD was defined.
- The most important aspects of BDD:
    * Requirements should be converted into user stories that can define concrete examples of the application.
    * Each example should be a valid user scenario.
    * An understanding of the ‘role-feature-reason’ matrix and the ‘give-when-then’ notation.
- Why is useful and when could be applied
    * Is useful because it gives stability to the build and code inside all project itself, it may be easier to apply when a project is just beginning.
- Witch type of teams could implement BDD
    * all teams that has a DEV and QA personal, also the previous approval of the Product Owner
- Structure of a feature: 
Feature: Information test
  Validate service retrieving information

  Scenario: Get information from Application to know if running
    Given I have all services up
    When I GET to /info
      And I send the request
    Then I should get a response with status code 200

- Structure of a user story

    As I have all services up,
    I want to get information about all services
    and response status code 200.