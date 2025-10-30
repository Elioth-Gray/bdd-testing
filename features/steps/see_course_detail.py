from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.service import Service
import os

CHROMEDRIVER_PATH = os.path.join(os.getcwd(), "chromedriver.exe")
BASE_URL = "https://buildwithangga.com"  

def find_element_by_locator_name(context, name):
    wait = WebDriverWait(context.driver, 3) 
    
    try:
        selector = f"[data-testid='{name}']"
        return wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, selector)))
    
    except TimeoutException:
        try:
            return wait.until(EC.visibility_of_element_located((By.ID, name)))
        
        except TimeoutException:
            try:
                selector = f".{name}" 
                return wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, selector)))
            
            except TimeoutException:
                raise AssertionError(
                    f"Failed to find element '{name}'"
                )

@given('I am on "{path}"')
def step_impl_visit_page(context, path):
    service = Service(CHROMEDRIVER_PATH)
    context.driver = webdriver.Chrome(service=service)
    context.driver.maximize_window()
    url = BASE_URL + path
    context.driver.get(url)

@when('I press "{button_text}"')
def step_impl_press_button(context, button_text):
    wait = WebDriverWait(context.driver, 3)\
    
    try:
        xpath = (
            f"//button[normalize-space()='{button_text}'] | "
            f"//input[@value='{button_text}'] | "
            f"//a[@role='button' and normalize-space()='{button_text}'] | "
            f"//a[span[normalize-space()='{button_text}']]"
        )
        element = wait.until(EC.element_to_be_clickable((By.XPATH, xpath)))
        element.click()
    except TimeoutException:
        raise AssertionError(f"Button or link with text '{button_text}' was not found or could not be clicked.")

@when('I follow "{link_text}"')
def step_impl_follow_link(context, link_text):
    wait = WebDriverWait(context.driver, 3)

    try:
        xpath = (
            f"//a[normalize-space()='{link_text}'] | "
            f"//a[.//text()[normalize-space()='{link_text}']]"
        )
        element = wait.until(EC.element_to_be_clickable((By.XPATH, f"({xpath})[1]")))
        element.click()
    except TimeoutException:
        raise AssertionError(f"Link with text '{link_text}' was not found or could not be clicked.")

@then('I should be on "{path}"')
def step_impl_check_url(context, path):
    wait = WebDriverWait(context.driver, 3)

    try:
        wait.until(EC.url_contains(path))
    except TimeoutException:
        current_url = context.driver.current_url
        raise AssertionError(f"Expected URL to contain '{path}', but was '{current_url}'.")

@then('I should see an "{element_name}" element')
def step_impl_see_element(context, element_name):
    try:
        element = find_element_by_locator_name(context, element_name)
        assert element.is_displayed(), f"Element '{element_name}' was found in the HTML but is not visible."
    except AssertionError as e:
        raise e
