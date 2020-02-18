# 함수 만들기 
def Location_sales(year_sm,year_lg):

    #변수 
    str_year_1 = year_sm+' ' 
    str_year_2 = year_lg +' '
    main_year = str_year_2[:-1]

    col_1 = '합계'
    col_2 = '도서'
    col_3 = '만화'
    col_4 = '음악'
    col_5 = '영화'

    # 2014_2015
    # 여기 예외처리 추가 
    # 동작 확인 완료 ! 에러도 동작도 둘다 잘동작 ! 
    Path = './data/Content_Sales_'+main_year+'.csv'
    try:    
        sales = pd.read_csv( Path, header=1, encoding='euc-kr')
        print('불러옴',sales.head())
    except Exception as e:
        print('error => ',e) # 눈으로 확인이 가능
        
    # 행정구역 
    # sales_2017.iloc[:,[1]]
    sales_location = sales.iloc[:,[1]]
    sales['행정구역'] = sales_location

    # 결측치 존재
    # - 포함 삭제 해야함 혹은 0으로 
    sales.replace('-', 0 ,inplace=True)

    
    # 이름변경
    state = sales.행정구역.iloc[:1] # 소계 => 전국
    seoul= sales.행정구역.iloc[1:2]# 소계 => 서울

    change={'소계':'서울'}
    chan={'소계':'전국'}

    seoul.replace(change,inplace=True)
    state.replace(chan,inplace=True)

    
    # 데이터 제거 
    # sales.columns[0:2]
    drop_col = sales.iloc[:,[0,1,7,13]]
    try:    
        sales.drop( drop_col, inplace=True, axis=1 )
        print("drop_col 제거>>> \n",sales.head(1) )
    except Exception as e:
        print('error => ',e) # 에러를 눈으로 확인
    
    # 열정리
    sales = sales.iloc[:,[10,0,1,2,3,4,5,6,7,8,9]]

    
    # sales.columns => 컬럼명 변경 
    cols = {
            sales.columns[1]: (str_year_1 + col_1),
            sales.columns[2]: (str_year_1 + col_2),
            sales.columns[3]: (str_year_1 + col_3),
            sales.columns[4]: (str_year_1 + col_4),
            sales.columns[5]: (str_year_1 + col_5),

            sales.columns[6]: (str_year_2 + col_1),
            sales.columns[7]: (str_year_2 + col_2),
            sales.columns[8]: (str_year_2 + col_3),
            sales.columns[9]: (str_year_2 + col_4),
            sales.columns[10]:(str_year_2 + col_5)

          }

    # print(cols)
    # 변경
    sales.rename(columns= cols, inplace= True)

    
    # int로 타입 변경 => 연산을 해야해서 정수로 
    # str_year_1 + col_1 = ' yyyy' +'합계'
    sales[str_year_1 + col_1]= sales[str_year_1 + col_1].astype(int)
    sales[str_year_1 + col_2]= sales[str_year_1 + col_2].astype(int)
    sales[str_year_1 + col_3]= sales[str_year_1 + col_3].astype(int)
    sales[str_year_1 + col_4]= sales[str_year_1 + col_4].astype(int)
    sales[str_year_1 + col_5]= sales[str_year_1 + col_5].astype(int)

    # 도서안에 만화책도 포함 
    sales['총합계']= sales[str_year_1 + col_1] + sales[str_year_2 + col_1]
    sales['총도서']= sales[str_year_1 + col_2] + sales[str_year_2 + col_2] + sales[str_year_1 + col_3] + sales[str_year_2 + col_3]
    sales['총음악']= sales[str_year_1 + col_4] + sales[str_year_2 + col_4]
    sales['총영화']= sales[str_year_1 + col_5] + sales[str_year_2 + col_5]

    
    # 최종확인 
    sales.head(10)
    
    # 엑셀 만들기 
    sales.to_csv("../data/output/sales_new_"+main_year+".csv", index=False)
    
    return sales


Location_sales()