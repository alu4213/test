Feature: Paginas Web estaticas en django

	Scenario: Home have content
		Given I access the url "/home/"
		Then I see the header "Sample App"

	Scenario: Help have content
		Given I access the url "/help/"
		Then I see the header "Help"

	Scenario: About have content
		Given I access the url "/about/"
		Then I see the header "About Us"

	Scenario: Home have title
		Given I access the url "/home/"
		Then I see the title "Home"

	Scenario: Help have title
		Given I access the url "/help/"
		Then I see the title "Help"

	Scenario: About have title
        Given I access the url "/about/"
        Then I see the title "About"