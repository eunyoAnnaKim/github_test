
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
import enterbrowser
import scroll



window_now = enterbrowser.window_now

def crawling_naver(driver = ''):
    driver.find_element(By.XPATH, '//*[@id="shortcutArea"]/ul/li[4]/a/span[1]').click()
    wait = WebDriverWait(driver,10)
    wait.until(ec.presence_of_element_located((By.TAG_NAME, "body")))
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
    wait.until(ec.presence_of_element_located((By.TAG_NAME, "body")))
    #새창으로 유알엘이 바뀌었는지 확인
    #newurl = driver.current_url
    #print(str(newurl))

    #섹션 넘겨서 '도서'로 진입
    driver.find_element(By.CSS_SELECTOR, '#content > div > div.shoppingHomeResponsive_inner__32dS_ > div > div.shoppingHomeResponsive_category__ub5P_ > div > button').click()
    wait.until(ec.presence_of_element_located((By.CLASS_NAME, "shoppingCategoryListResponsive_shopping_category_list_responsive__Km2Iz ")))
    driver.find_element(By.CSS_SELECTOR, '#content > div > div.shoppingHomeResponsive_inner__32dS_ > div > div.shoppingHomeResponsive_category__ub5P_ > div > div > ul:nth-child(1) > li:nth-child(8) > a > div.shoppingCategoryListResponsive_image_area__uOErR > svg').click()
    wait.until(ec.presence_of_element_located((By.TAG_NAME, "body")))
    #driver.find_element(By.CSS_SELECTOR, '#lnb > div > div > ul > li._lnb_lnb_book_RlNeu._lnb_list_2GxP2 > a').click()
    #time.sleep(5)

    #스크롤 최하단으로 이동해서 페이지 전부 열어주기
    scroll.scroll_to_bottom(driver)
    
    return driver