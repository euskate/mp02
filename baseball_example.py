##########################################
# 튜닝한 것 
# import necessary libraries
import warnings
warnings.filterwarnings("ignore")
from random import seed
from random import randrange
from csv import reader
from math import sqrt
import pandas as pd
import numpy as np
from numpy import random
import matplotlib.pyplot as plt
from prettytable import PrettyTable

from sklearn import preprocessing
from sklearn import linear_model
from sklearn.linear_model import SGDRegressor
from sklearn import preprocessing
from sklearn.metrics import mean_squared_error,mean_absolute_error
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.neighbors import KNeighborsRegressor
from sklearn.linear_model import RANSACRegressor
from sklearn.linear_model import LinearRegression
import mglearn

from subplot import make_plot
# 하이퍼파라미터 튜닝을 위한 그리드서치 클래스 임포트 
from sklearn.model_selection import GridSearchCV 


# 전체 타자 데이터
bat_total=pd.read_csv('/Users/admin/Dropbox/Rank_Predict/Data/MLB_data_edit/real_bat_total.csv')
# 전체 투수 데이터
pit_total=pd.read_csv('/Users/admin/Dropbox/Rank_Predict/Data/MLB_data_edit/real_pit_total.csv')
# 전체 랭크 데이터
rank_total=pd.read_csv('/Users/admin/Dropbox/Rank_Predict/Data/MLB_data_edit/rank_good.csv')
# 10년치 팀 평균(타자)
# R, 2B, HR, RBI, BB, SF, OBP, SLG, OPS 사용
b_total=pd.read_csv('/Users/admin/Dropbox/Rank_Predict/Data/MLB_data_edit/b_total_no_scale.csv')
# 10년치 팀 평균(투수)
# IP, K, ERA, WHIP 사용
p_total=pd.read_csv('/Users/admin/Dropbox/Rank_Predict/Data/MLB_data_edit/p_total_no_scale.csv')
# 득점률/방어율
r=pd.read_csv('/Users/admin/Dropbox/Rank_Predict/Data/MLB_data_edit/bat_r.csv')

del b_total['Unnamed: 0']
del p_total['Unnamed: 0']

# 타자, 투수 지표
p_corr=pit_total[['IP','K','ERA','WHIP']]
b_corr=b_total[['R','H','TH','AVG','SO','HBP','SB','2B','3B','HR','RBI','OPS']]

# 승률
rank_PCT=r[['R']]

# y = 승률, X = 투수지표
y=rank_PCT; X=b_corr

# scatter로 확인
make_plot()

# train 데이터와 test 데이터 정의 및 분리
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,shuffle=False)


# 표준화 함수 정의
sc = preprocessing.StandardScaler()
# 데이터를 표준화
sc.fit(X_train)
X_train_std = sc.transform(X_train)


sc.fit(X_test)
X_test_std = sc.transform(X_test)

clf_ = linear_model.LinearRegression() # 0.89
# clf_ = linear_model.Ridge(alpha=.5) # 0.88
# clf_ = linear_model.LassoLars(alpha=.1) #0.87
# clf_ = RANSACRegressor(random_state=None) #0.85
# clf_ = linear_model.MultiTaskLasso(alpha=0.1, random_state=None) #0.886
# clf_ = KNeighborsRegressor(n_neighbors=15) 0.70
# clf_ = linear_model.Lasso(alpha=0.1,max_iter=5000) 0.88


# 하이퍼 파라미터 튜닝 
parameters = {'normalize':[True]}
grid_clf_ = GridSearchCV(clf_, param_grid=parameters, cv=5, refit=True)

# 학습 
grid_clf_.fit(X_train, y_train) ## 
y_pred  = grid_clf_.predict(X_test) ##

# scatter 함수 구현
# plt.scatter(X_train.R,y_train)
# plt.grid()
# plt.xlabel('Actual X')
# plt.ylabel('Predicted y')
# plt.title('scatter plot between actual y and predicted y')
# plt.tight_layout()
# plt.show()


# 학습 정확도 확인
print("★학습 정확도 확인★")
print('GridSearchCV 최적 파라미터:',grid_clf_.best_params_)
print('GridSearchCV 최고 정확도: {0:.4f}'.format(grid_clf_.best_score_))
estimator = grid_clf_.best_estimator_
X_test_std = sc.transform(X_test)
y_pred = estimator.predict(X_test_std)
# print("테스트 데이터 세트 정확도: {0:.4f}".format(accuracy_score(y_test, y_pred)))






# 학습정확도 확인
print("★학습 정확도 확인_하이퍼파라미터 튜닝 추가 코드★")

print('Mean Squared Error :',mean_squared_error(y_test,y_pred))
print('Mean Absolute Error :',mean_absolute_error(y_test,y_pred))
print("train 학습 정확도 :", grid_clf_.score(X_train, y_train)) 
print("test 학습 정확도 :", grid_clf_.score(X_test, y_test)) 
