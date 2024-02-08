from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
import time

options = Options()
driver = webdriver.Chrome(options=options)
driver.maximize_window()
action = ActionChains(driver)
wait = WebDriverWait(driver,10)
url = ''
window_now = driver

def enter(url):
    window_now = driver.current_window_handle
    driver.get(url)
    wait.until(ec.presence_of_element_located((By.TAG_NAME, "body")))
    time.sleep(5)