import gspread
from oauth2client.service_account import ServiceAccountCredentials
from google.oauth2.service_account import Credentials
import time


def save_gspread(filename='', book_list = []):
    scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']

    credentials = ServiceAccountCredentials.from_json_keyfile_name('cred.json', scope)

    gc = gspread.authorize(credentials)

    new_spreadsheet = gc.create(filename)

    headers = list(book_list[0].keys())  # Assume all items in book_list have the same keys
    worksheet = new_spreadsheet.sheet1
    worksheet.insert_row(headers, index=1)

    for i, row in enumerate(book_list, start=2):  # 첫 번째 행은 헤더이므로 2부터 시작합니다.
        for j, (key, value) in enumerate(row.items(), start=1):
            worksheet.update_cell(i, j, value)
            time.sleep(2/3)

    new_spreadsheet.share("revliss@naver.com", perm_type='user', role='writer')
