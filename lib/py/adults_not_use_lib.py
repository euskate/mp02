

# 함수 생성 
def adults_lib(year):
    # 컬럼용 변수 
    year_ech = year + ' '
    
    
    # engine='python' = 한글 에러 방지 
#     Path = './data/Content_Sales_'+year+'.csv'
#     adults_not_use_lib =pd.read_csv('./data/성인이_공공도서관을_이용하지_않는_이유_'+year+'.csv', header =1 , encoding='euc-kr',engine='python')

    # 파일 불러오기 
    Path = './data/성인이_공공도서관을_이용하지_않는_이유_'+year+'.csv'
    try:    
        adults_not_use_lib = pd.read_csv( Path, header=1, encoding='euc-kr',engine='python')
        print('불러옴')
    except Exception as e:
        print('error => ',e) # 눈으로 확인이 가능

    
    # 컬럼 변경 : 사례수  => 참여수
    adults_not_use_lib.rename(columns= {adults_not_use_lib.columns[2] : '참여수'}, inplace= True)

    # 데이터프레임 제편성 
    adults_not_use_lib = adults_not_use_lib.iloc[:,2:]
    # 데이터 프레임 반전 
    adults_not_use_lib = adults_not_use_lib.T

    # 연도 추가  => 합치면 .... ? 

    # 재편성 
    adults_not_use_lib = adults_not_use_lib.iloc[:,[0,1,2,3,4,5,6,7]]

    # 컬럼명 수정 
    cols = {
    #         adults_not_use_lib.columns[0] : '연도',
            adults_not_use_lib.columns[0] : year_ech+'전체',
            adults_not_use_lib.columns[1] : year_ech+'남자',
            adults_not_use_lib.columns[2] : year_ech+'여자',
            adults_not_use_lib.columns[3] : year_ech+'20대',
            adults_not_use_lib.columns[4] : year_ech+'30대',
            adults_not_use_lib.columns[5] : year_ech+'40대',
            adults_not_use_lib.columns[6] : year_ech+'50대',
            adults_not_use_lib.columns[7] : year_ech+'60대이상'

          }
    adults_not_use_lib.rename(columns= cols, inplace= True)
    
    # 엑셀 만들기 
    adults_not_use_lib.to_csv("../data/output/adults_not_use_lib"+'_'+year+".csv", index=False)
    
    return adults_not_use_lib


# 파일이 존재하는 데이터만 읽음 
# 아니면 에러남 
# 파라메타는 str 형식으로 넣을것 !
adults_lib('2010')