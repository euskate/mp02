from selenium import webdriver
import urllib.request
import time
from selenium.webdriver.common.keys import Keys
import os
import win32com.client

# 날짜 리스트
dayList = [
    # ('2010-01-01', '2010-03-31'), ('2010-04-01', '2010-06-30'), ('2010-07-01', '2010-09-30'), ('2010-10-01', '2010-12-31'),
    # ('2011-01-01', '2011-03-31'), ('2011-04-01', '2011-06-30'), ('2011-07-01', '2011-09-30'), ('2011-10-01', '2011-12-31'),
    # ('2012-01-01', '2012-03-31'), ('2012-04-01', '2012-06-30'), ('2012-07-01', '2012-09-30'), ('2012-10-01', '2012-12-31'),
    # ('2013-01-01', '2013-03-31'), ('2013-04-01', '2013-06-30'), ('2013-07-01', '2013-09-30'), ('2013-10-01', '2013-12-31'),
    # ('2014-01-01', '2014-03-31'), ('2014-04-01', '2014-06-30'), ('2014-07-01', '2014-09-30'), ('2014-10-01', '2014-12-31'),
    ('2015-01-01', '2015-03-31'), ('2015-04-01', '2015-06-30'), ('2015-07-01', '2015-09-30'), ('2015-10-01', '2015-12-31'),
    ('2016-01-01', '2016-03-31'), ('2016-04-01', '2016-06-30'), ('2016-07-01', '2016-09-30'), ('2016-10-01', '2016-12-31'),
    ('2017-01-01', '2017-03-31'), ('2017-04-01', '2017-06-30'), ('2017-07-01', '2017-09-30'), ('2017-10-01', '2017-12-31'),
    ('2018-01-01', '2018-03-31'), ('2018-04-01', '2018-06-30'), ('2018-07-01', '2018-09-30'), ('2018-10-01', '2018-12-31'),
    ('2019-01-01', '2019-03-31'), ('2019-04-01', '2019-06-30'), ('2019-07-01', '2019-09-30'), ('2019-10-01', '2019-12-31')
]

# 품목 이름
name = 'pear'

# 크롤링 옵션 정하기
options = webdriver.ChromeOptions()

# options.add_argument('headless') #화면 표시 X
options.add_argument("disable-gpu")   
options.add_argument("lang=ko_KR")    
options.add_argument('user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36')  # user-agent 

# 2015 ~ 2019 3개월씩 크롤링 반복 
for startday, endday in dayList:

    # itemcategorycode : 부류 
    # 채소류 : 200, 과일류 : 400
    itemcategorycode = 400

    # itemcode : 품목
    # 무 : 231, 배추 : 211, 사과 : 411, 파 : 246, 배 : 412
    itemcode = 412

    # kindcode : 품종, 없으면 ''
    # 사과-후지 : 05, 배-신고 : 01
    kindcode = '01'

    # url : KAMIS 농수산물유통정보 사이트
    url = f"https://www.kamis.or.kr/customer/price/retail/period.do?action=daily&startday={startday}&endday={endday}&countycode=&itemcategorycode={itemcategorycode}&itemcode={itemcode}&kindcode={kindcode}&productrankcode=1&convert_kg_yn=N"

    # 셀레니움 실행 및 접속
    driver = webdriver.Chrome('./chromedriver.exe', options=options)
    driver.get(url)
    time.sleep(2)

    # 파일 저장
    target = driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/section[3]/div/a")
    target.click()
    time.sleep(3)
    driver.close()  

    # 파일 이름 변경
    path = 'C:/Users/admin/Downloads/'
    os.rename(f'{path}가격정보.xls', f'{path}{startday}_{name}.xls')
    time.sleep(1)

    # xls 읽기 에러가 난다 -> xlsx로 변경
    xl = win32com.client.Dispatch("Excel.Application")
    path = path.replace('/','\\')
    wb = xl.Workbooks.Open(f'{path}{startday}_{name}.xls')
    wb.SaveAs(f'{path}{startday}_{name}.xlsx', FileFormat = 51)
    wb.Close()
    xl.Quit()
    time.sleep(1)

    # 파일 삭제
    path = 'C:/Users/admin/Downloads/'
    os.remove(f'{path}{startday}_{name}.xls')
    time.sleep(0.5)
