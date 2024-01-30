from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time


driver = webdriver.Chrome()
driver.maximize_window()
action = ActionChains(driver)
driver.get("https://search.shopping.naver.com/book/home")
time.sleep(2)
prev_height = driver.execute_script("return document.body.scrollHeight")
while True:
    # 스크롤을 화면 가장 아래로 내린다
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    
    # 페이지 로딩 대기
    time.sleep(2)

    # 현재 문서 높이를 가져와서 저장
    curr_height = driver.execute_script("return document.body.scrollHeight")

    if(curr_height == prev_height):
        break
    else:
        prev_height = driver.execute_script("return document.body.scrollHeight")

driver.find_element(By.PARTIAL_LINK_TEXT, '가정/요리').click()
time.sleep(5)
booktitle = []
elems_title = driver.find_elements(By.CLASS_NAME, 'bookListItem_text__bglOw')
for elem_title in elems_title:
    title = elem_title.get_property