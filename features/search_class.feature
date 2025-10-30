Feature: Search Class on BuildWithAngga
  As a user
  I want to search for classes
  So that I can find the class I want

  Scenario: Search Class Success
    Given I am on "/"
    When I press "search button"
    Then I should see an "modal-content" element
    When I fill in "keyword" with "UI Design"
    Then I should see an "course-card" element

  Scenario: Clear Search Field After Typing
    Given I am on "/"
    When I press "search button"
    Then I should see an "modal-content" element
    When I fill in "keyword" with "UI Design"
    And I clear the field "keyword"
    Then I should see an "text-danger" element
    And I should see the text "Keyword tidak boleh kosong"

  Scenario: Search With Less Than 3 Characters
    Given I am on "/"
    When I press "search button"
    Then I should see an "modal-content" element
    When I fill in "keyword" with "UI"
    Then I should see an "text-danger" element
    And I should see the text "Minimal 3 karakter"

  Scenario: Search Non-Existent Class
    Given I am on "/"
    When I press "search button"
    Then I should see an "modal-content" element
    When I fill in "keyword" with "Alien Cooking"
    Then I should see an "no-result" element
    And I should see the text "Kelas tidak ditemukan"
