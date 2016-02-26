Feature: Logging in

  Scenario: valid login
    given I access "http://www.meuspedidos.com.br"
    when I click in "Fazer Login"
    and I log in with valid credentials
    then I check I am logged in as "Henrique"
