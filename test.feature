Feature: Logging in

  Scenario: valid login
    given I access "http://69.164.203.63:8080"
    when I click in "Fazer Login"
    and I log in with valid credentials
    then I check I am logged in as "Henrique"
