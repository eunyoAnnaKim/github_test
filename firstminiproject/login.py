from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import pyperclip

def log_in(driver = ''):
    #로그인
    wait = WebDriverWait(driver, 10)
    action = ActionChains(driver)
    driver.find_element(By.CLASS_NAME, 'gnb_txt').click()
    wait.until(ec.presence_of_element_located((By.TAG_NAME, "body")))
    driver.find_element(By.ID, "id").click()
    pyperclip.copy("revliss")
    action.key_down(Keys.COMMAND).send_keys('v').key_up(Keys.COMMAND).perform()
    driver.find_element(By.ID, "pw").click()
    pyperclip.copy("Knitevery365!")
    action.key_down(Keys.COMMAND).send_keys('v').key_up(Keys.COMMAND).perform()

    driver.find_element(By.ID, "log.login").click()
    wait.until(ec.presence_of_element_located((By.TAG_NAME, "body")))
    driver.find_element(By.ID, 'new.dontsave').click()
    wait.until(ec.presence_of_element_located((By.TAG_NAME, "body")))

    return driver