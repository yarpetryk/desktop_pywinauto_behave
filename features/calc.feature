@calc
Feature: Calculator
    Scenario Outline: Test Calculator functionality 
        Given I start the App
        When I find button "<num_1>" and click
        When I find button "<operation>" and click
        When I find button "<num_2>" and click
        When I find button "<result>" and click
        Then The text "<expected_result>" should be visible

        Examples:
            | num_1   | operation | num_2 | result | expected_result |
            | One     | Plus      | Two   | Equals | 3               |
            | Seven   | Minus     | Two   | Equals | 6               |
            


