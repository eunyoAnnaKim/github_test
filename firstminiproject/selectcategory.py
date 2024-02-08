from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
import enternaverbook
import scroll

#태그선택

def select_category(driver = ''):
    tag_list = driver.find_elements(By.CLASS_NAME, 'category_link_category__XlcyC')
    tag_string =', '.join([tag.text for tag in tag_list])
    select_tag = input(f'원하는 카테고리를 입력하세요 :\n[{tag_string}]\n')
    
    for tag in tag_list:
        if tag.text == select_tag:
            tag.click()
            break
    wait = WebDriverWait(driver, 10)
    wait.until(ec.presence_of_element_located((By.TAG_NAME, "body")))

    #새롭게 로드된 창에 핸들저장?? 다시 확인하기
    new_window = driver.window_handles[-1]
    driver.switch_to.window(new_window)

    # 새 창에서 URL을 가져옵니다.
    new_window_url = driver.current_url
    #print("새 창의 URL:", new_window_url)

    scroll.scroll_to_bottom(driver)

    print(select_tag)
    return select_tag
    
