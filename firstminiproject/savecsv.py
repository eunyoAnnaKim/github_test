from datetime import datetime
import selectcategory, csv, getdata




def save_csv( book_list = [], select_tag= '' ):
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
    
    return  filename
