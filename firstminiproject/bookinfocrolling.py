from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
import scroll as scrolltobottom


driver = webdriver.Chrome()
driver.maximize_window()
action = ActionChains(driver)
driver.get("https://search.shopping.naver.com/book/home")
time.sleep(2)
scrolltobottom.scroll_to_bottom(driver)

driver.find_element(By.PARTIAL_LINK_TEXT, '가정/요리').click()
time.sleep(3)

new_window = driver.window_handles[-1]
driver.switch_to.window(new_window)

# 새 창에서 URL을 가져옵니다.
new_window_url = driver.current_url
#print("새 창의 URL:", new_window_url)

scrolltobottom.scroll_to_bottom(driver)

for i in range(1,11):
    onebook = driver.find_elements(By.XPATH, '//*[@id="book_list"]/ul/li['+str(i)+']')
    for onebookdata in onebook:
        eachbook = []
        eachbook = onebookdata.text.split('\n')
        print(eachbook)


왠열 맥북에 엑셀이없어서 진행이 불가..
