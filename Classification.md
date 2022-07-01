# 분류  
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

# 붓꽃 데이터 호출
from sklearn.datasets import load_iris
iris = load_iris()

print(iris.DESCR)

data = iris.data
label = iris.target
columns = iris.feature_names

data = pd.DataFrame(data, columns = columns)
data.head()

data.shape

data.describe()

data.info()
```

* Logistic Regression  
가운데 회귀선을 통해 분류를 할 수 있다. 이럴 때 사용하는 것이 Logistic Regression 이다.  
마찬가지로 SVC, Decision Tree 등을 사용할 수 도 있다.

``` python
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(data, label, 
                                                    test_size=0.2, shuffle=True, stratify=label, random_state=2019)

from sklearn.linear_model import LogisticRegression
lr = LogisticRegression()

lr.fit(x_train, y_train)

y_pred = lr.predict(x_test)

from sklearn.metrics import accuracy_score

print('로지스틱 회귀, 정확도 : {:.2f}%'.format(accuracy_score(y_test, y_pred)*100))

```


