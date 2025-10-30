Feature: Search and Filter Tips
  As a user
  I want to find relevant technical tips
  So that I can improve my skills

  Scenario: User finds and views a specific tip
    Given I am on "/"
    When I follow "Tips Terbaru"
    And I fill in "search-input" with "Nest.js"
    And I press "Search"
    And I follow "Panduan Lengkap Nest.js untuk Pemula: Cara Membuat REST API dengan Framework Node.js Modern"
    Then the url should contain "/tips/panduan-lengkap-nestjs-untuk-pemula"
    And I should see "Panduan Lengkap Nest.js untuk Pemula"
    And I close the browser

  Scenario: User searches using a non-existent keyword
    Given I am on "/tips"
    When I fill in "search-input" with "Judi Online"
    And I press "Search"
    Then I should see text "Saat ini tips belum tersedia"
    And I close the browser

  Scenario: User filters tips by category
    Given I am on "/tips"
    When I follow "Backend Development"
    Then the url should contain "/tips/category/backend-development"
    And I should see "Tips Backend Development"
    And I close the browser

  Scenario: User attempts to search with an empty keyword
    Given I am on "/tips"
    When I press "Search"
    Then the "search-input" element should possess the "required" attribute
    And I close the browser

  Scenario: User attempts to search with a keyword that is too short
    Given I am on "/tips"
    When I fill in "search-input" with "a"
    Then the "search-input" element should have attribute "minlength" with value "2"
    And I close the browser