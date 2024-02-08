from enterbrowser import enter
import enterbrowser
from enternaverbook import crawling_naver
from selectcategory import select_category
from getdata import get_data
from savecsv import save_csv
from login import log_in
from mailling import send_mail
from savegspread import save_gspread


#select_site = input('다음의 사이트중 선택해주세요 :')
site_list = ['네이버', '알라딘', '예스24', '교보문고']
site_urls = {
    '네이버': 'https://www.naver.com',
    '알라딘': 'https://www.aladin.co.kr',
    '예스24': 'https://www.yes24.com',
    '교보문고': 'https://www.kyobobook.co.kr'
}
select_site = input(f'사이트를 선택하세요 : ')
if select_site in site_list:
    url = site_urls[select_site]
     



enter(url)
driver = enterbrowser.driver
crawling_naver(driver)
select_tag = select_category(driver)
book_list = get_data(driver)
filename = save_csv(book_list, select_tag)
driver = log_in(driver)
#send_mail(driver, filename)
save_gspread(filename, book_list)