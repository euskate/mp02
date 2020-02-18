import pandas as pd
import os

# 폴더명 이름 'data_{name}'
name = 'scallion'

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