Feature: See Course Detail
  As a user
  I want to be able to see the details of a course
  So that I can view its curriculum and lessons

  Scenario: See Class Detail Success
    Given I am on "/"
    When I press "Kelas" 
    Then I should see an "dropdown-menu" element 
    When I follow "Graphic Design" 
    Then I should be on "/belajar/graphic-design"
    And I should see an "courseContainer" element 
    And I should see an "link-course-title" element 
    When I follow "Web Development: Build a Freelancer Portfolio with Webflow"
    Then I should be on "/kelas/web-development-build-a-freelancer-portfolio-with-webflow?main_leads=topic"
    And I should see an "header-primary" element 
    And I should see an "content-lessons" element 
    And I should see an "item-pricing" element