from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import pytest


@pytest.fixture(scope='function')
def driver():
    # options = Options()
    # options.add_argument('--headless')
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


def test_part_one(driver):
    data = 'DarthVader'
    driver.get('https://www.qa-practice.com/elements/input/simple')
    text_input = driver.find_element(By.CSS_SELECTOR, '#id_text_string')
    text_input.send_keys(data)
    text_input.send_keys(Keys.ENTER)
    text_result = driver.find_element(By.CSS_SELECTOR, '#result-text')
    print(text_result.text)


def test_part_two(driver):
    driver.get('https://demoqa.com/automation-practice-form')
    first_name = driver.find_element(By.CSS_SELECTOR, '#firstName')
    first_name.send_keys('Johnny')
    last_name = driver.find_element(By.CSS_SELECTOR, '#lastName')
    last_name.send_keys('Depp')
    email = driver.find_element(By.CSS_SELECTOR, '#userEmail')
    email.send_keys('Depp@gmail.com')
    gender = driver.find_element(By.XPATH, '//*[text()="Male"]')
    gender.click()
    mobile = driver.find_element(By.CSS_SELECTOR, '#userNumber')
    mobile.send_keys('8987478596')
    date_of_birth = driver.find_element(By.CSS_SELECTOR, '#dateOfBirthInput')
    date_of_birth.click()
    month = driver.find_element(By.XPATH, '//option[text()="June"]')
    month.click()
    year = driver.find_element(By.XPATH, '//option[text()="1963"]')
    year.click()
    day = driver.find_element(By.XPATH, '//*[@aria-label="Choose Sunday, June 9th, 1963"]')
    day.click()
    subjects = driver.find_element(By.CSS_SELECTOR, '#subjectsInput')
    subjects.click()
    subjects.send_keys('Movie')
    hobbies = driver.find_element(By.XPATH, '//*[text()="Music"]')
    hobbies.click()
    address = driver.find_element(By.CSS_SELECTOR, '#currentAddress')
    address.send_keys('USA')
    driver.find_element(By.CSS_SELECTOR, '#currentAddress').send_keys(Keys.PAGE_DOWN)
    state = driver.find_element(By.CSS_SELECTOR, '#state')
    state.click()
    state = driver.find_element(By.XPATH, '//*[text()="Haryana"]')
    state.click()
    city = driver.find_element(By.CSS_SELECTOR, '#city')
    city.click()
    city = driver.find_element(By.XPATH, '//*[text()="Karnal"]')
    city.click()
    submit_btn = driver.find_element(By.CSS_SELECTOR, '#submit')
    submit_btn.click()
    modal = driver.find_element(By.CSS_SELECTOR, '.modal-body').text
    print(modal)


def test_part_three1(driver):
    driver.get('https://www.qa-practice.com/elements/select/single_select')
    drop_down = driver.find_element(By.CSS_SELECTOR, '[value="1"]')
    drop_down_text = drop_down.text
    drop_down.click()
    submit_btn = driver.find_element(By.CSS_SELECTOR, '#submit-id-submit')
    submit_btn.click()
    text_result = driver.find_element(By.CSS_SELECTOR, '#result-text')
    assert drop_down_text == text_result.text, 'The texts do not match'


def test_part_three2(driver):
    driver.get('https://the-internet.herokuapp.com/dynamic_loading/2')
    start_btn = driver.find_element(By.XPATH, '//*[text()="Start"]')
    start_btn.click()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#finish')))
    text_result = driver.find_element(By.XPATH, '//*[text()="Hello World!"]').text
    assert text_result == 'Hello World!', 'The texts do not match'
