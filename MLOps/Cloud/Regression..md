# Regression
``` python
import os
from os.path import join
import copy
import warnings
warnings.filterwarnings('ignore')

import numpy as np
import pandas as pd

import sklearn

import matplotlib.pyplot as plt

# 보스턴 데이터 집값 불러오기
from sklearn.datasets import load_boston
boston = load_boston()

print(boston.DESCR)

data = boston.data
label = boston.target
columns = boston.feature_names

data = pd.DataFrame(data, columns = columns)
data.head()

data.shape
data.describe()
data.info()
```

* Linear Regression  
선형 회귀의 첫 번째로 x가 1개인 단순 회귀 분석에 대해 실습해보겠습니다.
x 변수로 'RM' 변수를, y 변수는 주택 가격으로 하겠습니다.
Linear Regression은 Sklearn의 linear_model 패키지에 있습니다.  
  
회귀부터는 데이터를 train, test로 나누어 진행하겠습니다. sklearn의 model_selection 패키지에 있는 train_test_split 함수를 사용합니다.  

``` python

'''4가지로 split 하는 코드이다. 학습용 데이터 x_train, 학습용 라벨 y_train, 테스트 데이터 x_test, 테스트 라벨 y_test'''
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(data, label, test_size=0.2, random_state=2019)

# 선형 회귀 사용 (대다수의 경우 잘 맞지 않다.)
from sklearn.linear_model import LinearRegression
sim_lr = LinearRegression()

sim_lr.fit(x_train['RM'].values.reshape((-1, 1)), y_train)

y_pred = sim_lr.predict(x_test['RM'].values.reshape((-1, 1)))

from sklearn.metrics import r2_score

print('단순 선형 회귀, R2 : {:.4f}'.format(r2_score(y_test, y_pred)))

line_x = np.linspace(np.min(x_test['RM']), np.max(x_test['RM']), 10)
line_y = sim_lr.predict(line_x.reshape((-1, 1)))

plt.scatter(x_test['RM'], y_test, s=10, c='black')
plt.plot(line_x, line_y, c = 'red')
plt.legend(['Regression line', 'Test data sample'], loc='upper left')

print('단순 선형 회귀, 계수(w) : {:.4f}, 절편(b) : {:.4f}'.format(sim_lr.coef_[0], sim_lr.intercept_))
# 결과 : 단순 선형 회귀, 계수(w) : 9.9900, 절편(b) : -40.0941
```

* Decision Tree Regressor  
결정트리로 회귀하는 것. 선형보다 조금 더 정확함을 볼 수 있다.
``` python
from sklearn.tree import DecisionTreeRegressor
dt_regr = DecisionTreeRegressor(max_depth=5)

dt_regr.fit(x_train['RM'].values.reshape((-1, 1)), y_train)

y_pred = dt_regr.predict(x_test['RM'].values.reshape((-1, 1)))

print('단순 결정 트리 회귀, R2 : {:.4f}'.format(r2_score(y_test, y_pred)))

line_x = np.linspace(np.min(x_test['RM']), np.max(x_test['RM']), 10)
line_y = dt_regr.predict(line_x.reshape((-1, 1)))

# 다른 데이터가 추가되면 급격히 떨어진다.
plt.scatter(x_test['RM'].values.reshape((-1, 1)), y_test, c = 'black')
plt.plot(line_x, line_y, c = 'red')
plt.legend(['Regression line', 'Test data sample'], loc='upper left')

```

* SVR (Support Vector Machine Regressor)  
선을 계속 긋는 것인데, 마진이 조금더 큰 벡터를 기준으로 생각을 한다.
``` python
from sklearn.svm import SVR
svm_regr = SVR()

svm_regr.fit(x_train['RM'].values.reshape((-1, 1)), y_train)

y_pred = svm_regr.predict(x_test['RM'].values.reshape((-1, 1)))

print('단순 서포트 벡터 머신 회귀, R2 : {:.4f}'.format(r2_score(y_test, y_pred)))

line_x = np.linspace(np.min(x_test['RM']), np.max(x_test['RM']), 100)
line_y = svm_regr.predict(line_x.reshape((-1, 1)))

plt.scatter(x_test['RM'], y_test, c = 'black')
plt.plot(line_x, line_y, c = 'red')
plt.legend(['Regression line', 'Test data sample'], loc='upper left')


```