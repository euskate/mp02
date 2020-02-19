from selenium import webdriver
import urllib.request
import time
from selenium.webdriver.common.keys import Keys
import os
import win32com.client
import shutil
import pandas as pd

def crawl_agri(name, day, category, item, kind):
    """
    크롤링을 하는 함수
    """
    # 크롤링 옵션 정하기
    options = webdriver.ChromeOptions()

    # options.add_argument('headless') #화면 표시 X
    options.add_argument("disable-gpu")   
    options.add_argument("lang=ko_KR")    
    options.add_argument('user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36')  # user-agent 

    # 2015 ~ 2019 3개월씩 크롤링 반복 
    for startday, endday in dayList:

        # url : KAMIS 농수산물유통정보 사이트
        url = f"https://www.kamis.or.kr/customer/price/retail/period.do?action=daily&startday={startday}&endday={endday}&countycode=&itemcategorycode={itemcategorycode}&itemcode={itemcode}&kindcode={kindcode}&productrankcode=1&convert_kg_yn=N"

        # 셀레니움 실행 및 접속
        driver = webdriver.Chrome('./webdriver/chromedriver.exe', options=options)
        driver.get(url)
        time.sleep(2)

        # 파일 저장
        target = driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/section[3]/div/a")
        target.click()
        time.sleep(3)
        driver.close()  

        # 폴더 만들기
        path = 'C:/Users/admin/Downloads/'
        if not os.path.exists(f'{path}data_{name}'):
            os.mkdir(f'{path}data_{name}')
        
        # 파일 이름 변경
        os.rename(f'{path}가격정보.xls', f'{path}{startday}_{name}.xls')
        time.sleep(1)

        # xls 읽기 에러가 난다 -> xlsx로 변경
        xl = win32com.client.Dispatch("Excel.Application")
        path = path.replace('/','\\')
        wb = xl.Workbooks.Open(f'{path}{startday}_{name}.xls')
        wb.SaveAs(f'{path}data_{name}\\{startday}_{name}.xlsx', FileFormat = 51)
        wb.Close()
        xl.Quit()
        time.sleep(1)

        # 파일 삭제
        path = 'C:/Users/admin/Downloads/'
        os.remove(f'{path}{startday}_{name}.xls')
        time.sleep(0.5)
    
    ### 폴더 이동하기
    shutil.move(f'{path}data_{name}', f'{os.getcwd()}/data/data_{name}')

def to_dataframe(name):
    # 파일 목록 가져오기
    files = os.listdir(f'./data/data_{name}')

    df_result = pd.DataFrame(columns=[0, 1, 'year', 'month', 'day'])

    for file in files:
        # 엑셀 데이터 프레임 만들기
        df = pd.read_excel(f'./data/data_{name}/{file}', nrows=2)
        # 뒤집기
        df = df.T
        # 필요없는 데이터 삭제
        df.drop(index=df.iloc[:3].index, inplace=True)
        ## 2010~2014년도 더미 에러 추가 코드 : 더미 데이터가 있을 경우 삭제하고 아니면 패스하라.
        try:
            df.drop(index=df[df.index.str.contains('Unnamed') == True].index, inplace=True)
        except:
            pass    
        # 파일명에서 연도 가져오기
        year = file[:4]
        # 인덱스 리셋하기
        df = df.reset_index()
        # 연,월,일 설정
        df['year'] = year
        df['month'] = df['index'].dt.month
        df['day'] = df['index'].dt.day
        # index 삭제
        del df['index']
        df_result = pd.concat([df_result, df])

    # 컬럼명 변경
    df_result.rename(columns={0:'평균', 1:'평년'}, inplace=True)

    # 날짜 컬럼 만들기
    df_result['date'] = pd.to_datetime(df_result[['year','month','day']])

    # # 컬럼 순서 조정
    df_result = pd.DataFrame(df_result, columns=['date', '평균', '평년'])

    # 데이터 타입 변경, 결측치는 0으로 세팅
    df_result['평균'] = df_result['평균'].str.replace(',', '').str.replace('-','0').astype(int)
    df_result['평년'] = df_result['평년'].str.replace(',', '').str.replace('-','0').astype(int)

    # 컬럼명 2차 변경
    df_result.rename(columns={'평균':f'avg_{name}', '평년':f'avgY_{name}'}, inplace=True)

    # 확인
    print(df_result.columns)
    print(df_result.head())
    print(df_result.shape)
    print(df_result.dtypes)

    # CSV 파일로 만들기
    df_result.to_csv(f'./data/result_{name}.csv', encoding="utf-8", index=False)

# #### 변수 설정

# dayList = [
#     ('2015-01-01', '2015-03-31'), ('2015-04-01', '2015-06-30'), ('2015-07-01', '2015-09-30'), ('2015-10-01', '2015-12-31'),
#     ('2016-01-01', '2016-03-31'), ('2016-04-01', '2016-06-30'), ('2016-07-01', '2016-09-30'), ('2016-10-01', '2016-12-31'),
#     ('2017-01-01', '2017-03-31'), ('2017-04-01', '2017-06-30'), ('2017-07-01', '2017-09-30'), ('2017-10-01', '2017-12-31'),
#     ('2018-01-01', '2018-03-31'), ('2018-04-01', '2018-06-30'), ('2018-07-01', '2018-09-30'), ('2018-10-01', '2018-12-31'),
#     ('2019-01-01', '2019-03-31'), ('2019-04-01', '2019-06-30'), ('2019-07-01', '2019-09-30'), ('2019-10-01', '2019-12-31')
# ] # 날짜 리스트
# name = 'pear' # 품목 이름
# itemcategorycode = 400  # itemcategorycode : 부류   # 채소류 : 200, 과일류 : 400
# itemcode = 412  # itemcode : 품목   # 무 : 231, 배추 : 211, 사과 : 411, 파 : 246, 배 : 412

# kindcode = '01' # kindcode : 품종, 없으면 '' # 사과-후지 : 05, 배-신고 : 01


# 날짜 리스트
dayList = [
    ('2010-01-01', '2010-03-31'), ('2010-04-01', '2010-06-30'), ('2010-07-01', '2010-09-30'), ('2010-10-01', '2010-12-31'),
    ('2011-01-01', '2011-03-31'), ('2011-04-01', '2011-06-30'), ('2011-07-01', '2011-09-30'), ('2011-10-01', '2011-12-31'),
    ('2012-01-01', '2012-03-31'), ('2012-04-01', '2012-06-30'), ('2012-07-01', '2012-09-30'), ('2012-10-01', '2012-12-31'),
    ('2013-01-01', '2013-03-31'), ('2013-04-01', '2013-06-30'), ('2013-07-01', '2013-09-30'), ('2013-10-01', '2013-12-31'),
    ('2014-01-01', '2014-03-31'), ('2014-04-01', '2014-06-30'), ('2014-07-01', '2014-09-30'), ('2014-10-01', '2014-12-31'),
    # ('2015-01-01', '2015-03-31'), ('2015-04-01', '2015-06-30'), ('2015-07-01', '2015-09-30'), ('2015-10-01', '2015-12-31'),
    # ('2016-01-01', '2016-03-31'), ('2016-04-01', '2016-06-30'), ('2016-07-01', '2016-09-30'), ('2016-10-01', '2016-12-31'),
    # ('2017-01-01', '2017-03-31'), ('2017-04-01', '2017-06-30'), ('2017-07-01', '2017-09-30'), ('2017-10-01', '2017-12-31'),
    # ('2018-01-01', '2018-03-31'), ('2018-04-01', '2018-06-30'), ('2018-07-01', '2018-09-30'), ('2018-10-01', '2018-12-31'),
    # ('2019-01-01', '2019-03-31'), ('2019-04-01', '2019-06-30'), ('2019-07-01', '2019-09-30'), ('2019-10-01', '2019-12-31')
]

# 품목 이름
name = 'moo'

# itemcategorycode : 부류 
# 채소류 : 200, 과일류 : 400
itemcategorycode = 200

# itemcode : 품목
# 무 : 231, 배추 : 211, 사과 : 411, 파 : 246, 배 : 412
itemcode = 231

# kindcode : 품종, 없으면 ''
# 사과-후지 : 05, 배-신고 : 01
kindcode = ''




if __name__ == "__main__":
    # crawl_agri(name=name, day=dayList, category=itemcategorycode, item=itemcode, kind=kindcode)
    to_dataframe(name=name)


