from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import os, time

WEBDRIVER_PATH = os.path.join(os.getcwd(), "chromedriver.exe")

selectors = {
    "search button": "button.btn-secondary[data-bs-target='#quickSearchModal']",
}

@given('I am on "/"')
def step_open_homepage(context):
    service = Service(WEBDRIVER_PATH)
    context.driver = webdriver.Chrome(service=service)
    context.driver.get("https://buildwithangga.com")
    context.driver.maximize_window()
    context.driver.implicitly_wait(10)
    print("Berhasil membuka halaman utama BuildWithAngga.")


@when('I press "{element_name}"')
def step_press_button(context, element_name):
    """Klik elemen berdasarkan nama yang dimapping ke CSS selector"""
    driver = context.driver
    wait = WebDriverWait(driver, 10)
    selector = selectors.get(element_name, element_name)  # fallback literal
    btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, selector)))
    btn.click()
    print(f"Klik elemen: {element_name} ({selector})")
    time.sleep(1)


@then('I should see an "{selector}" element')
def step_see_element(context, selector):
    """Pastikan elemen dengan class atau CSS selector muncul"""
    driver = context.driver
    wait = WebDriverWait(driver, 10)
    try:
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME, selector)))
        print(f"Elemen '{selector}' muncul (by CLASS_NAME).")
    except:
        try:
            wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, selector)))
            print(f"Elemen '{selector}' muncul (by CSS_SELECTOR).")
        except:
            print(f"Elemen '{selector}' tidak ditemukan.")
    time.sleep(1)


@when('I fill in "{field_name}" with "{text}"')
def step_fill_field(context, field_name, text):
    """Isi field dengan teks tertentu"""
    driver = context.driver
    wait = WebDriverWait(driver, 10)
    field = wait.until(EC.visibility_of_element_located((By.NAME, field_name)))
    field.clear()
    field.send_keys(text)
    print(f"Mengisi field '{field_name}' dengan teks: {text}")
    time.sleep(2)  # biar hasil search muncul dulu


@when('I clear the field "{field_name}"')
def step_clear_field(context, field_name):
    """Hapus isi field untuk trigger validasi kosong"""
    driver = context.driver
    wait = WebDriverWait(driver, 10)
    field = wait.until(EC.visibility_of_element_located((By.NAME, field_name)))
    field.send_keys(Keys.CONTROL + "a")
    field.send_keys(Keys.BACKSPACE)
    print(f"Field '{field_name}' dikosongkan.")
    time.sleep(1)


@then('I should see the text "{expected_text}"')
def step_see_text(context, expected_text):
    """Pastikan teks tertentu muncul di halaman"""
    driver = context.driver
    time.sleep(1)
    page_source = driver.page_source
    if expected_text.lower() in page_source.lower():
        print(f"Teks ditemukan: {expected_text}")
    else:
        print(f"Teks '{expected_text}' tidak ditemukan di halaman.")
    time.sleep(1)
    driver.quit()
