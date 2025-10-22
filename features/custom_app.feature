@custom_app
Feature: CANHacker App
    Scenario: Test Settings
    Given I start the App
    When I proceed to menu "Settings"
    When I select checkbox "RTS HS"
    When I select "4800 bit/s" in dropdown "2"
    When I find button "Ok" and click
    When I proceed to menu "Settings"
    Then The checkbox "RTS HS" is selected
    Then The item "4800 bit/s" in dropdown "2" is selected