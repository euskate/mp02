# 라이브러리 불러오기
import pandas as pd
import numpy as np

def mergeAgriWheather(agriList):
    # 데이터 프레임 불러오기 : 농산물
    for var in agriList:  # 농산물 데이터프레임
        globals()[f'df_{var}'] = pd.read_csv(f'./data/result_{var}.csv')
        globals()[f'df_{var}'].rename(columns={'date':'날짜'}, inplace=True)
        globals()[f'df_{var}']['날짜'] = pd.to_datetime(globals()[f'df_{var}']['날짜'])
        
    # 데이터 프레임 불러오기 : 날씨
    df_wheather = pd.read_csv('./data/date_final.csv')  # 날씨 데이터프레임

    # 데이터 타입 변경
    df_wheather['날짜'] = pd.to_datetime(df_wheather.날짜)
    # 추가 코드 : 날짜 형식 변경
    try:
        df_wheather['날짜'] = df_wheather['날짜'].dt.strftime('%y-%m-%d')
    except:
        pass
    df_wheather['현재기온'] = pd.to_numeric(df_wheather['현재기온'], errors='coerce')
    df_wheather['이슬점온도'] = pd.to_numeric(df_wheather['이슬점온도'], errors='coerce')
    df_wheather['체감온도'] = pd.to_numeric(df_wheather['체감온도'], errors='coerce')
    # df_wheather['강수량'] = pd.to_numeric(df_wheather['강수량'], errors='coerce')
    df_wheather['습도'] = pd.to_numeric(df_wheather['습도'], errors='coerce')
    df_wheather['풍속'] = pd.to_numeric(df_wheather['풍속'], errors='coerce')
    df_wheather['해면기압'] = pd.to_numeric(df_wheather['해면기압'], errors='coerce')

    # 농산물 데이터 병합
    df_agri = pd.DataFrame(data=globals()[f'df_{agriList[0]}'])
    for var in agriList[1:] :
        df_agri = pd.merge(df_agri, globals()[f'df_{var}'], on='날짜')

    # 농산물 및 날씨 데이터 병합
    df = pd.merge(df_agri, df_wheather, on='날짜')

    # 데이터 확인
    print(df.head())
    print(df.info())

    # CSV 파일로 출력
    df.to_csv('./data/merge_agri_wheather.csv', encoding='utf-8', index=False)


# 농산물 리스트
# agriList = ['moo', 'baechoo', 'apple', 'scallion', 'pear']
agriList = ['moo']

if __name__ == "__main__":
    mergeAgriWheather(agriList=agriList)