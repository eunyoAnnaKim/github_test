import time, scroll, csv, pyperclip
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException

#브라우저 옵션과 기본 설정들
driver = webdriver.Chrome(options=Options())
driver.maximize_window()
action = ActionChains(driver)



starturl = "https://naver.com"

#현재의 창 핸들에 저장
window_now = driver.current_window_handle
driver.get(starturl)
time.sleep(2)
driver.find_element(By.XPATH, '//*[@id="shortcutArea"]/ul/li[4]/a/span[1]').click()
time.sleep(2)

#모든창을 핸들에 저장
allwindows = driver.window_handles
newwindow = None
#모든창(항상 두개)중에 새롭게 열린창을 찾아서 newwindow에 저장
for window in allwindows:
    if window != window_now:
        newwindow = window
        #driver에는 여전히 먼저열린 창이 핸들에 저장되있어서 그 창을 닫기
        driver.close()

#newwindow로 driver 변경
driver.switch_to.window(newwindow)
time.sleep(2)
#새창으로 유알엘이 바뀌었는지 확인
#newurl = driver.current_url
#print(str(newurl))

#섹션 넘겨서 '도서'로 진입
driver.find_element(By.CSS_SELECTOR, '#content > div > div.shoppingHomeResponsive_inner__32dS_ > div > div.shoppingHomeResponsive_category__ub5P_ > div > button').click()
time.sleep(1)
driver.find_element(By.CSS_SELECTOR, '#content > div > div.shoppingHomeResponsive_inner__32dS_ > div > div.shoppingHomeResponsive_category__ub5P_ > div > button.N\=a\:scut\.right.pagingButtonPc_paging_button_pc__u2Qcq.pagingButtonPc_next__C1obE').click()
time.sleep(1)
driver.find_element(By.CSS_SELECTOR, '#content > div > div.shoppingHomeResponsive_inner__32dS_ > div > div.shoppingHomeResponsive_category__ub5P_ > div > div > ul > li:nth-child(1) > a > div.shoppingCategoryListResponsive_image_area__uOErR > svg').click()
time.sleep(2)
scroll.scroll_to_bottom(driver)

#태그선택
tag_list = driver.find_elements(By.CLASS_NAME, 'category_link_category__XlcyC')
tag_string =', '.join([tag.text for tag in tag_list])

select_tag = input(f'원하는 카테고리를 입력하세요 :\n[{tag_string}]\n')

for tag in tag_list:
    if tag.text == select_tag:
        tag.click()
        break

time.sleep(2)

new_window = driver.window_handles[-1]
driver.switch_to.window(new_window)

scroll.scroll_to_bottom(driver)

#열로 데이터 가져오기

countneeddata = int(input("원하는 책의 권수를 선택하세요 :"))
#countneeddata = 100
page_count = countneeddata//40
lastpagedata = countneeddata%40
if lastpagedata > 0:
    page_count += 1
countgetdata = 0

#책정보를 담을 배열을 만들고 그안에 담을 데이터를 추출
book_list = []

for page in range(page_count):
    scroll.scroll_to_bottom(driver)
    #책정보가 나타나는 창의 데이터를 모두 가져옴
    books =driver.find_elements(By.CLASS_NAME, 'bookListItem_item_inner__Fp7hN')
    for book in books:
        
        #여럿의 데이터를 각각으로 만든다
        #한 권의 책정보를 모두 담을 그릇인 딕셔너리(키값과 벨류값을 알아서 지정해주기때문에 유용!)
        book_info = {}

        #책제목
        try:
            title_parent_element = book.find_element(By.CLASS_NAME, 'bookListItem_text__bglOw')
            bigtitle_element = title_parent_element.find_element(By.CSS_SELECTOR, 'div.bookListItem_title__X7f9_ > span > span:nth-child(1)')
            book_info['bigtitle'] = bigtitle_element.text.strip()
        except NoSuchElementException:
            book_info['bigtitle'] = ' '

        try:
            title_parent_element = book.find_element(By.CLASS_NAME, 'bookListItem_text__bglOw')
            smalltitle_element = title_parent_element.find_element(By.CSS_SELECTOR, 'div.bookListItem_title__X7f9_ > span > span:nth-child(2)')
            book_info['smalltitle'] = smalltitle_element.text.strip()
        except NoSuchElementException:
            book_info['smalltitle'] = ' '

        #순위
        try:
            rank_element = book.find_element(By.CLASS_NAME, 'bookListItem_feature__txTlp')
            book_info['rank'] = rank_element.text.strip()
        except NoSuchElementException:
            book_info['rank'] = ' '
        
        #저자
        try:
            writer_parent_element = book.find_element(By.CLASS_NAME, 'bookListItem_define_item__LdTib')
            writer_element = writer_parent_element.find_element(By. CLASS_NAME, 'bookListItem_define_data__kKD8t')
            book_info['writer'] = writer_element.text.strip()
        except NoSuchElementException:
            book_info['writer'] = ' '
        
        #출판사
        try:
            publisher_parent_element = book.find_element(By.CLASS_NAME, 'bookListItem_detail_publish__FgPYQ')
            publisher_element = publisher_parent_element.find_element(By.CLASS_NAME, 'bookListItem_define_data__kKD8t')
            book_info['publisher'] = publisher_element.text.strip()
        except NoSuchElementException:
            book_info['publisher'] = ' '
        
        #출간일
        try:
            dayeofpublication_element = book.find_element(By.CLASS_NAME, 'bookListItem_detail_date___byvG')
            book_info['dayeofpublication'] = dayeofpublication_element.text.strip()
        except NoSuchElementException:
            book_info['dayeofpublication'] = ' '

        #별점평가
        try:
            reviewscore_element = book.find_element(By.CLASS_NAME, 'bookListItem_grade__tywh2')
            book_info['reviewscore'] = reviewscore_element.text.strip()
        except NoSuchElementException:
            book_info['reviewscore'] = ' '

        #일반도서가격
        try:
            price_parent_element = book.find_element(By.CLASS_NAME, 'bookListItem_sub_info__AfkOO')
            bookprice_element = price_parent_element.find_element(By.CSS_SELECTOR, 'div:nth-child(1) > span')
            book_info['price'] = bookprice_element.text.strip()
            
        except NoSuchElementException:
            book_info['price'] = ' '
            
        try:
            price_parent_element = book.find_element(By.CLASS_NAME, 'bookListItem_sub_info__AfkOO')
            ebookprice_element = price_parent_element.find_element(By.CSS_SELECTOR, 'div:nth-child(2) > span')
            book_info['ebookprice'] = ebookprice_element.text.strip()
        except NoSuchElementException:
            book_info['ebookprice'] = ' '

        try:
            price_parent_element = book.find_element(By.CLASS_NAME, 'bookListItem_sub_info__AfkOO')
            audiobookprice_element = price_parent_element.find_element(By.CSS_SELECTOR, 'div:nth-child(3) > span')
            book_info['audiobookprice'] = audiobookprice_element.text.strip()
        except NoSuchElementException:
            book_info['audiobookprice'] = ' '

        countgetdata += 1
        if countgetdata >= countneeddata+1:
            break
        #만들어진 한 권의 정보(딕셔너리)를 북리스트(배열)에 저장
        book_list.append(book_info)

    if countgetdata >= countneeddata+1:
        break

    if page < page_count-1:
        driver.find_element(By.CLASS_NAME, 'Paginator_btn_next__0pdVd').click()
        time.sleep(2)
        
    
print(book_list)# [{첫번째책}, {두번째책}, ...]

#csv파일에 딕셔너리를 집어넣기위해 각 인덱스의 필드명을 지정
fieldnames = ['bigtitle', 'smalltitle', 'rank', 'writer', 'publisher', 'dayeofpublication', 'reviewscore', 'price', 'ebookprice', 'audiobookprice']
#파일네임 지정
today = datetime.today().strftime('%Y%m%d')
filename = today + select_tag + "도서목록.csv"
#writeheader로 필드명을 면저 넣어주고, 리스트안의 자료를 각각 eachbook으로 뽑아와서 행으로 넣어줌
with open(filename, mode='w', newline='', encoding='utf-8-sig') as file:
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    for eachbook in book_list:
        writer.writerow(eachbook)
    
#로그인
driver.find_element(By.CLASS_NAME, 'gnb_txt').click()
time.sleep(2)
driver.find_element(By.ID, "id").click()
pyperclip.copy("revliss")
action.key_down(Keys.COMMAND).send_keys('v').key_up(Keys.COMMAND).perform()
driver.find_element(By.ID, "pw").click()
pyperclip.copy("Knitevery365!")
action.key_down(Keys.COMMAND).send_keys('v').key_up(Keys.COMMAND).perform()

driver.find_element(By.ID, "log.login").click()
time.sleep(3)

driver.find_element(By.ID, 'new.dontsave').click()
time.sleep(3)

#로그인후 마지막에서 열려있던 창에서 '메일'로 진입
driver.find_element(By.CLASS_NAME, 'mail_li').click()
time.sleep(3)

#나에게쓰기로 진입. 엑스패스값만 들어가는데.. 크게 바뀔일이 없는 자료라 일단 넘어감
driver.find_element(By.CSS_SELECTOR, '#root > div > nav > div > div.lnb_header > div.lnb_task > a.item.button_write_to_me').click()
time.sleep(2)
driver.find_element(By.CSS_SELECTOR, '#subject_title').send_keys(filename)
time.sleep(2)

#파일첨부는 inputbox로 되어있었다..! 경로를 바로 입력해 파일을 불러옴
driver.find_element(By.CSS_SELECTOR, '#ATTACH_LOCAL_FILE_ELEMENT_ID').send_keys(f"/Users/macintosh/Desktop/eunyo/workspace/github/{filename}")
time.sleep(3)

pyperclip.copy("내용")
driver.find_element(By.CLASS_NAME, 'editor_body').click()
action.key_down(Keys.COMMAND).send_keys('v').key_up(Keys.COMMAND).perform()
#driver.find_element(By.CLASS_NAME, 'workseditor-content').send_keys("내용")
time.sleep(3)
driver.find_element(By.CSS_SELECTOR,'button.button_write_task').click()
time.sleep(3)

# DataFrame 생성
df = pd.DataFrame(book_list)

# 가격 정보에서 '최저'와 '원'을 제거하고 숫자로 변환
df['price'] = df['price'].str.replace('최저 ', '').str.replace('원', '').str.replace(',', '').astype(int)

# 평점 정보에서 괄호 안의 숫자를 제거하고 숫자로 변환
df['rank'] = df['rank'].str.extract(r'(\d+\.\d+)')
df['rank'] = df['rank'].astype(float)

# 시각화
plt.figure(figsize=(10, 6))
plt.scatter(df['price'], df['rank'], color='blue', alpha=0.5)
plt.title('Book Price vs. Rank')
plt.xlabel('Price (KRW)')
plt.ylabel('Rank')
plt.grid(True)
plt.show()