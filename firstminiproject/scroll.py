import time

def scroll_to_bottom(driver):
    prev_height = driver.excute_script("return document.body.scrollHeight")
    while True:
        driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        time.sleep(1)
        curr_height = driver.execute_script("return document.body.scrollHeight")
        if(curr_height == prev_height):
            break
        else:
            prev_height = driver.execute_script("return document.body.scrollHeight")