from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import scroll
import selectcategory




#책정보를 담을 배열을 만들고 그안에 담을 데이터를 추출


def get_data(driver='', book_list = []):
    countneeddata = int(input("원하는 책의 권수를 선택하세요 :"))
    #countneeddata = 5

    page_count = countneeddata//40
    lastpagedata = countneeddata%40
    if lastpagedata > 0:
        page_count += 1
    countgetdata = 0

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
            wait = WebDriverWait(driver, 10)
            wait.until(ec.presence_of_element_located((By.TAG_NAME, "body")))
    print(book_list)
    return book_list
    # [{첫번째책}, {두번째책}, ...]
