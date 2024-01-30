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
time.sleep(3)



bookcontent = driver.find_element(By.CSS_SELECTOR, '#book_list > ul')
eachbook = bookcontent.find_elements(By.CSS_SELECTOR, 'bookListItem_item_book__1yCey')
book_title = []
for booklist in eachbook:
    booktitle = booklist.find_element(By.XPATH, '//*[@id="book_list"]/ul/li/div/a[1]/div[2]/div[1]/span/span[1]')
    book_title.append(booktitle.text)

print(book_title)