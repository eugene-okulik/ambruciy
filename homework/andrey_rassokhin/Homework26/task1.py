from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import pytest


@pytest.fixture(scope='function')
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


def test_part1(driver):
    driver.get('http://testshop.qa-practice.com/')
    product = driver.find_element(By.CSS_SELECTOR, '[alt="Customizable Desk"]')
    action = ActionChains(driver)
    action.key_down(Keys.CONTROL).click(product).key_up(Keys.CONTROL).perform()
    tabs = driver.window_handles
    driver.switch_to.window(tabs[1])
    add_to_card_btn = driver.find_element(By.CSS_SELECTOR, '#add_to_cart')
    add_to_card_btn.click()
    WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.XPATH, '//*[text()="Continue Shopping"]'))).click()
    WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.XPATH, '//*[text()="Item(s) added to your cart"]')))
    driver.close()
    driver.switch_to.window(tabs[0])
    basket_link = driver.find_element(By.CSS_SELECTOR, '.o_wsale_my_cart')
    basket_link.click()
    result = driver.find_element(By.CSS_SELECTOR, '.align-top').text
    assert result == 'Customizable Desk (Steel, White)'


def test_part2(driver):
    driver.get('https://magento.softwaretestingboard.com/gear/bags.html')
    try:
        cookie = (
            WebDriverWait(driver, 3).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, '[aria-label="Consent"]'))))
        cookie.click()
    except TimeoutException:
        print('Модалка с куками не появилась')
    finally:
        bags = driver.find_element(By.CSS_SELECTOR, '.item.product.product-item')
        add_to = driver.find_element(
            By.XPATH, '//*[@title="Add to Compare" and contains(@data-post,"14")]')
        action = ActionChains(driver)
        action.move_to_element(bags)
        action.click(add_to)
        action.perform()
        (WebDriverWait(driver, 3).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '[data-ui-id = "message-success"]'))))
        result = (WebDriverWait(driver, 3).until(
            EC.presence_of_element_located((
                By.XPATH, '//a[text()="Push It Messenger Bag"]'))).text)
        assert result == 'Push It Messenger Bag'
