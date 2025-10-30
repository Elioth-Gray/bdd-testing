from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.service import Service
import time
import os

# Path definition
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
CHROMEDRIVER_PATH = os.path.join(PROJECT_ROOT, "chromedriver.exe")
BASE_URL = "https://buildwithangga.com"

def find_element_by_locator_name(context, name):
    wait = WebDriverWait(context.driver, 10)
    try:
        return wait.until(EC.visibility_of_element_located((By.ID, name)))
    except TimeoutException:
        try:
            selector = f".{name}"
            return wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, selector)))
        except TimeoutException:
            raise AssertionError(f"Failed to find element '{name}' using ID or class.")

# --- Step Definitions ---
@given('I am on "{path}"')
def step_impl_visit_page(context, path):
    service = Service(CHROMEDRIVER_PATH)
    context.driver = webdriver.Chrome(service=service)
    context.driver.maximize_window()
    
    url = BASE_URL + (path if path != "/" else "")
    context.driver.get(url)

@when('I fill in "{element_id}" with "{text}"')
def step_impl_fill_field(context, element_id, text):
    element = find_element_by_locator_name(context, element_id)
    element.clear()
    element.send_keys(text)

@when('I press "{button_text}"')
def step_impl_press_button(context, button_text):
    wait = WebDriverWait(context.driver, 10)
    try:
        xpath = f"//button[normalize-space()='{button_text}']"
        element = wait.until(EC.element_to_be_clickable((By.XPATH, xpath)))
        element.click()
    except TimeoutException:
        raise AssertionError(f"Button with text '{button_text}' was not found or could not be clicked.")

@when('I follow "{link_text}"')
def step_impl_follow_link(context, link_text):
    wait = WebDriverWait(context.driver, 10)
    try:
        element = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, link_text)))
        element.click()
    except TimeoutException:
        raise AssertionError(f"Link with text '{link_text}' was not found or could not be clicked.")

@then('I should see "{text}"')
def step_impl_see_text(context, text):
    """Checks for a given text within any element on the page."""
    wait = WebDriverWait(context.driver, 10)
    try:
        wait.until(EC.visibility_of_element_located(
            (By.XPATH, f"//h1[contains(text(), '{text}')]")
        ))
    except TimeoutException:
        raise AssertionError(f"Text '{text}' was not found on the page.")
    
@then('I should see text "{text}"')
def step_impl_see_text(context, text):
    """Checks for a given text within any element on the page."""
    wait = WebDriverWait(context.driver, 10)
    try:
        wait.until(EC.visibility_of_element_located(
            (By.XPATH, f"//*[contains(text(), '{text}')]")
        ))
    except TimeoutException:
        raise AssertionError(f"Text '{text}' was not found on the page.")

@then('the url should contain "{path}"')
def step_impl_check_url(context, path):
    wait = WebDriverWait(context.driver, 10)
    try:
        wait.until(EC.url_contains(path))
    except TimeoutException:
        current_url = context.driver.current_url
        raise AssertionError(f"Expected URL to contain '{path}', but was '{current_url}'.")

@then('the "{element_id}" element should possess the "{attribute}" attribute')
def step_impl_element_has_attribute(context, element_id, attribute):
    element = find_element_by_locator_name(context, element_id)
    assert element.get_attribute(attribute) is not None, f"Attribute '{attribute}' not found on '{element_id}'."

@then('the "{element_id}" element should have attribute "{attribute}" with value "{value}"')
def step_impl_element_has_attribute_value(context, element_id, attribute, value):
    element = find_element_by_locator_name(context, element_id)
    actual_value = element.get_attribute(attribute)
    assert actual_value == value, f"Attribute '{attribute}' had value '{actual_value}', not '{value}'."

@then('I close the browser')
def step_impl_close_browser(context):
    context.driver.quit()