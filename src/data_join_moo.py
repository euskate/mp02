# 라이브러리 불러오기
import pandas as pd
import numpy as np

# 데이터 불러오기
df_moo = pd.read_csv('./data/result_df.csv')
df_wheather = pd.read_csv('./data/date_final.csv')

# 데이터 확인
print(df_moo.head())
print(df_moo.dtypes)
print(df_wheather.head())
print(df_wheather.dtypes)
print(df_wheather.columns)

# 컬럼명 변경
df_moo.rename(columns={'date':'날짜'}, inplace=True)

# 데이터 타입 변경
df_moo['날짜'] = pd.to_datetime(df_moo.날짜)
df_wheather['날짜'] = pd.to_datetime(df_wheather.날짜)
df_wheather['현재기온'] = pd.to_numeric(df_wheather['현재기온'], errors='coerce')
df_wheather['이슬점온도'] = pd.to_numeric(df_wheather['이슬점온도'], errors='coerce')
df_wheather['체감온도'] = pd.to_numeric(df_wheather['체감온도'], errors='coerce')
df_wheather['강수량'] = pd.to_numeric(df_wheather['강수량'], errors='coerce')
df_wheather['습도'] = pd.to_numeric(df_wheather['습도'], errors='coerce')
df_wheather['풍속'] = pd.to_numeric(df_wheather['풍속'], errors='coerce')
df_wheather['해면기압'] = pd.to_numeric(df_wheather['해면기압'], errors='coerce')

# 확인
print(df_wheather.columns)
print(df_wheather.dtypes)
print(df_moo.dtypes)

# 데이터 병합
df = pd.merge(df_moo, df_wheather, on='날짜')

# 데이터 확인
print(df.head())

# CSV 파일로 출력
df.to_csv('./data/join_moo_wheather.csv', encoding='utf-8', index=False)