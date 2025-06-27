Feature: App
  @QA-4
  Scenario Outline: : Test Login
    Then Loign to application using "<username>" and "password"

    Examples:
      | username                           | password     |
      | automation_testuser@symphonyai.com | Welcome@2025 |