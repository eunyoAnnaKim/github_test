from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import pyperclip
import time
def send_mail(driver = '', filename = ''):
    #로그인후 마지막에서 열려있던 창에서 '메일'로 진입
    
    wait = WebDriverWait(driver, 10)
    element = wait.until(ec.element_to_be_clickable((By.CLASS_NAME, 'mail_li')))
    element.click()
    #driver.find_element(By.CLASS_NAME, 'mail_li').click()
    
    
    #나에게쓰기로 진입. 엑스패스값만 들어가는데.. 크게 바뀔일이 없는 자료라 일단 넘어감
    element = wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, '#root > div > nav > div > div.lnb_header > div.lnb_task > a.item.button_write_to_me')))
    element.click()
    wait.until(ec.presence_of_element_located((By.TAG_NAME, "body")))
    element = wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, '#subject_title')))
    element.send_keys(filename)
    

    #파일첨부는 inputbox로 되어있었다..! 경로를 바로 입력해 파일을 불러옴
    driver.find_element(By.CSS_SELECTOR, '#ATTACH_LOCAL_FILE_ELEMENT_ID').send_keys(f"/Users/macintosh/Desktop/eunyo/workspace/github/firstminiproject/{filename}")
    wait.until(ec.presence_of_element_located((By.TAG_NAME, "body")))

    pyperclip.copy("내용")
    driver.find_element(By.CLASS_NAME, 'editor_body').click()
    action = ActionChains(driver)
    action.key_down(Keys.COMMAND).send_keys('v').key_up(Keys.COMMAND).perform()
    #driver.find_element(By.CLASS_NAME, 'workseditor-content').send_keys("내용")
    time.sleep(5)
    element = wait.until(ec.element_to_be_clickable((By.CLASS_NAME,'button_write_task')))
    element.click()
    wait.until(ec.presence_of_element_located((By.TAG_NAME, "body")))
    
    return print('전송완료')