# import os

# itemcode = 211
# itemcategorycode = 200
# startday = '2015-01-01'

# path = 'C:/Users/admin/Downloads'
# os.rename(f'{path}/가격정보.xls', f'{path}/{itemcategorycode}{itemcode}_{startday}.xls')

import os, shutil

# 폴더명 이름 'data_{name}'
name = 'a'

# # 파일 목록 가져오기
# files = os.listdir(f'./data/data_{name}')

# print(files)

# for file in files:
#     category = file[:6]
#     datename = file[7:-5]
#     # print(category)
#     # print(datename)
#     os.rename(f'./data/data_{name}/{file}', f'./data/data_{name}/{datename}_{category}.xlsx')


### 폴더 만들기
path = 'C:/Users/admin/Downloads/'

if not os.path.exists(f'{path}/data_{name}'):
    os.mkdir(f'{path}/data_{name}')

### 폴더 이동하기
shutil.move(f'{path}/data_{name}', f'{os.getcwd()}/data/data_{name}')