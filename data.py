from crawl_def import crawl_agri as step1, to_dataframe as step2
from merge_agri_wheather import mergeAgriWheather as step3
from maindata_plus_tornado import plusTornado as step4

##### 변수 설정 #####

### 전체 변수
name = 'pear' # 이름 : 폴더명, 파일명, 컬럼명에 사용된다. 전체 step에 사용

### step1 변수 : 크롤링
# dayList : 크롤링할 기간, 3개월 단위
dayList = [
    ('2015-01-01', '2015-03-31'), ('2015-04-01', '2015-06-30'), ('2015-07-01', '2015-09-30'), ('2015-10-01', '2015-12-31'),
    ('2016-01-01', '2016-03-31'), ('2016-04-01', '2016-06-30'), ('2016-07-01', '2016-09-30'), ('2016-10-01', '2016-12-31'),
    ('2017-01-01', '2017-03-31'), ('2017-04-01', '2017-06-30'), ('2017-07-01', '2017-09-30'), ('2017-10-01', '2017-12-31'),
    ('2018-01-01', '2018-03-31'), ('2018-04-01', '2018-06-30'), ('2018-07-01', '2018-09-30'), ('2018-10-01', '2018-12-31'),
    ('2019-01-01', '2019-03-31'), ('2019-04-01', '2019-06-30'), ('2019-07-01', '2019-09-30'), ('2019-10-01', '2019-12-31')
]
# itemcategorycode : 분류 / 채소류 : 200, 과일류 : 400
itemcategorycode = 400 
# itemcode : 품목 / 무 : 231, 배추 : 211, 사과 : 411, 파 : 246, 배 : 412
itemcode = 412  
# kindcode : 품종 없으면 '' / 사과-후지 : 05, 배-신고 : 01
kindcode = '01' 

### step2 : 데이터프레임화
# 변수 : name

### step3 변수 : merge 합치기
# agriList : 합칠 농산물 목록
agriList = ['moo', 'baechoo', 'apple', 'scallion', 'pear']

### step4 변수 : 태풍 컬럼 더하기
# resultfilename : 최종 파일명
resultfilename = f'maindata_{len(agriList)}'

### 전체 실행
step1(name=name, day=dayList, category=itemcategorycode, item=itemcode, kind=kindcode)
step2(name=name)
step3(agriList=agriList)
step4(resultfilename=resultfilename)