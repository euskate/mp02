# 태풍 데이터를 추가하는 모듈
# 이환씨 코딩 자료

import pandas as pd
import numpy as np
from datetime import datetime

# class PlusTornado:
    
#     def __init__(self, resultfilename):
#         resultfilename = resultfilename
def plusTornado(resultfilename):

    # 데이터 불러온다.
    maindata = pd.read_csv('./data/merge_agri_wheather.csv')

    # 태풍 컬럼 만들고, x로 채운다.
    li = ['x' for i in range(maindata.shape[0])]
    maindata['태풍'] = li

    # 날짜 컬럼 변경
    def reduce_date(date):
        date = date.split('-')
        fdate = datetime(int(date[0]), int(date[1]), int(date[2]))
        return fdate
    maindata['날짜'] = maindata['날짜'].apply(reduce_date)

    # 토네이도 적용
    def tornado(date):
        istornado = (date >= datetime(2015,  6, 30) and date <= datetime(2015,  7, 26))  or \
                    (date >= datetime(2015,  8, 14) and date <= datetime(2015,  8, 25))  or \
                    (date >= datetime(2016,  9, 12) and date <= datetime(2016,  9, 20))  or \
                    (date >= datetime(2016,  9, 27) and date <= datetime(2016, 10,  5))  or \
                    (date >= datetime(2017,  7,  2) and date <= datetime(2017,  7,  4))  or \
                    (date >= datetime(2017,  7, 21) and date <= datetime(2017,  8,  8))  or \
                    (date >= datetime(2017,  9,  9) and date <= datetime(2017,  9, 18))  or \
                    (date >= datetime(2018,  6, 29) and date <= datetime(2018,  7,  4))  or \
                    (date >= datetime(2018,  8, 15) and date <= datetime(2018,  8, 24))  or \
                    (date >= datetime(2018,  9, 21) and date <= datetime(2018, 10,  1))  or \
                    (date >= datetime(2019,  7, 16) and date <= datetime(2019,  7, 20))  or \
                    (date >= datetime(2019,  8,  4) and date <= datetime(2019,  8, 16))  or \
                    (date >= datetime(2019,  9,  2) and date <= datetime(2019,  9,  8))  or \
                    (date >= datetime(2019,  9, 19) and date <= datetime(2019,  9, 23))  or \
                    (date >= datetime(2019,  9, 28) and date <= datetime(2019, 10,  3))
        if istornado:
            return "o"
        else:
            return "x"
    maindata['태풍'] = maindata['날짜'].apply(tornado)

    # 최종 CSV 파일명
    maindata.to_csv(f'./data/{resultfilename}.csv', index=False, encoding='UTF-8')