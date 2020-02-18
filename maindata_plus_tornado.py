# 태풍 데이터를 추가하는 모듈
# 이환씨 코딩 자료

import pandas as pd
import numpy as np
from datetime import datetime

maindata = pd.read_csv('./data/merge_agri_wheather.csv')

li = ['x' for i in range(maindata.shape[0])]

maindata['태풍'] = li

def reduce_date(date):
    date = date.split('-')
    fdate = datetime(int(date[0]), int(date[1]), int(date[2]))
    return fdate
maindata['날짜'] = maindata['날짜'].apply(reduce_date)

"""2015-06-30 ~ 2015-07-26
2015-08-14 ~ 2015-08-25
2016-09-12 ~ 2016-09-20
2016-09-27 ~ 2016-10-05
2017-07-02 ~ 2017-07-04
2017-07-21 ~ 2017-08-08
2017-09-09 ~ 2017-09-18
2018-06-29 ~ 2018-07-04
2018-08-15 ~ 2018-08-24
2018-09-21 ~ 2018-10-01
2019-07-16 ~ 2019-07-20
2019-08-04 ~ 2019-08-16
2019-09-02 ~ 2019-09-08
2019-09-19 ~ 2019-09-23
2019-09-28 ~ 2019-10-03
"""
start = datetime(2015, 6, 30)
end   = datetime(2015, 7, 26)

# maindata[ maindata.날짜 >= start ][maindata.날짜 <= end]
li = ['o' for i in range(maindata[ maindata.날짜 >= start ][maindata.날짜 <= end].shape[0])]

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

start = datetime(2015, 6, 30)
end   = datetime(2015, 7, 26)

# 최종 CSV 파일명
maindata.to_csv('./data/maindata_all.csv', index=False, encoding='UTF-8')