from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
import time

driver = webdriver.Firefox(executable_path="C:/webdriver/geckodriver.exe")
driver.maximize_window()
wait = WebDriverWait(driver, 100)


# Access URL
def geturl():
    driver.get("https://www.amaysim.com.au/")
    account = driver.find_element(By.XPATH, "//span[contains(@class,'variant-a')]//span[contains(text(),'Account')]")
    account.click()
    time.sleep(3)

# Login
def login():
    wait.until(EC.element_to_be_clickable((By.ID, "username"))).click()
    user = driver.find_element(By.ID, "username")
    user.send_keys('0466134574')
    pw = driver.find_element(By.ID, "password")
    pw.send_keys('AWqasde321')
    button = driver.find_element(By.NAME, "button")
    button.click()

# Account Profile
def access_profile():
    wait.until(EC.element_to_be_clickable((By.XPATH, "//h3[normalize-space()='My New Sim Nickname']"))).click()
    time.sleep(2)

# Access Refer a friend
def access_refer():
    wait.until(EC.element_to_be_clickable((By.XPATH, "//a[normalize-space()='Refer a friend']"))).click()
    time.sleep(15)

# TC1 - Refer a friend
def test_refer_friend():
    geturl()
    login()
    access_profile()
    access_refer()
    frame_id_locator = driver.find_element(By.CSS_SELECTOR, "#fb-6620b73c-b93f-48b8-ace5-792902216939")
    wait.until(EC.frame_to_be_available_and_switch_to_it(frame_id_locator))
    email_field = driver.find_element(By.ID, "a")
    email_field.send_keys('jefcoronel@gmail.com')
    time.sleep(2)
    button_css_locator = driver.find_element(By.CSS_SELECTOR, "#c")
    button_css_locator.click()
    frame_id_locator = driver.find_element(By.CSS_SELECTOR, "#fb-6620b73c-b93f-48b8-ace5-792902216939")
    wait.until(EC.frame_to_be_available_and_switch_to_it(frame_id_locator))
    driver.implicitly_wait(3)
    share_again = driver.find_element(By.ID, "w")
    wait.until(EC.element_to_be_clickable(share_again)).click()

# TC2 - Multiple Email
def test_multiple_emails():
    frame_id_locator = driver.find_element(By.CSS_SELECTOR, "#fb-6620b73c-b93f-48b8-ace5-792902216939")
    wait.until(EC.frame_to_be_available_and_switch_to_it(frame_id_locator))
    email_field = driver.find_element(By.ID, "a")
    email_field.send_keys('jefcoronel@gmail.com,johnfranciscoronel@gmail.com')
    time.sleep(2)
    button_css_locator = driver.find_element(By.CSS_SELECTOR, "#c")
    button_css_locator.click()
    driver.implicitly_wait(3)
    share_again = driver.find_element(By.ID, "w")
    wait.until(EC.element_to_be_clickable(share_again)).click()

# TC3 - Refer a friend - Blank Email field
def test_blank_email():
    frame_id_locator = driver.find_element(By.CSS_SELECTOR, "#fb-6620b73c-b93f-48b8-ace5-792902216939")
    wait.until(EC.frame_to_be_available_and_switch_to_it(frame_id_locator))
    time.sleep(2)
    button_css_locator = driver.find_element(By.CSS_SELECTOR, "#c")
    button_css_locator.click()

# TC4 - Refer a friend - Invalid Email format
def test_invalid_email():
    frame_id_locator = driver.find_element(By.CSS_SELECTOR, "#fb-6620b73c-b93f-48b8-ace5-792902216939")
    wait.until(EC.frame_to_be_available_and_switch_to_it(frame_id_locator))
    email_field = driver.find_element(By.ID, "a")
    email_field.send_keys('jefcoronel')
    time.sleep(2)
    button_css_locator = driver.find_element(By.CSS_SELECTOR, "#c")
    button_css_locator.click()

# TC5 - Blank Message field
def test_blank_message():
    frame_id_locator = driver.find_element(By.CSS_SELECTOR, "#fb-6620b73c-b93f-48b8-ace5-792902216939")
    wait.until(EC.frame_to_be_available_and_switch_to_it(frame_id_locator))
    driver.find_element(By.ID, "a").send_keys('@gmail.com')
    driver.find_element(By.ID, "b").clear()
    time.sleep(2)
    button_css_locator = driver.find_element(By.CSS_SELECTOR, "#c")
    button_css_locator.click()

# TC6 - Blank Email and Message field
def test_blank_fields():
    frame_id_locator = driver.find_element(By.CSS_SELECTOR, "#fb-6620b73c-b93f-48b8-ace5-792902216939")
    wait.until(EC.frame_to_be_available_and_switch_to_it(frame_id_locator))
    driver.find_element(By.ID, "a").clear()
    driver.find_element(By.ID, "b").clear()
    time.sleep(2)
    button_css_locator = driver.find_element(By.CSS_SELECTOR, "#c")
    button_css_locator.click()

def test_teardown():
    driver.close()
    driver.quit()
    print("Test Completed")

