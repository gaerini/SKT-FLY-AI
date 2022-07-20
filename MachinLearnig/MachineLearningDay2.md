# Machine Learning Day2

1. 사이킷런 파라미터  
여기서 가장 많이 다룰 것은 C와 감마이다.  

2. UCI사이트
UCI사이트는 머신러닝을 공부하기 위한 데이터들을 다운 받을 수 있는 곳이다. 하지만 정리되어있지 않다. 

3. 10_svm_breast_cancer.ipynb  

    ``` python
    import numpy as np
    import pandas as pd
    import matplotlib.pyplot as plt
    import seaborn as sns
    ```

    ``` python
    #사이킷런에 있는 유방암 데이터셋을 가져오는 과정
    from sklearn import datasets

    data = datasets.load_breast_cancer()
    type(data) #data는 딕셔너리 자료형이다.
    ```

    ``` python
    data.keys() # 우리가 사용할 수 있는 키들을 볼 수 있다.

    data['feature_names'], len(data['feature_names']) #피쳐가 무엇이 몇개 있는지 확인할 수 있다.
    ```

    ``` python
    #X값 만들기
    df_X = pd.DataFrame(data.data, columns=data.feature_names)

    df_X.shape
    ```

    ``` python
    # y 값 만들기
    df_y = pd.DataFrame(data.target, columns=['targets'])

    df_y.shape
    ```

    ``` python
    data.isna().sum(axis = 1)
    
    df_X.info()

    df_y.value_counts() # 1과 0이 몇개인지 확인하여 학습용 데이터와 훈련 데이터에 같은 분포로 만들기 위한 참조를 한다.
    ```

    ``` python
    # 학습/테스트 데이터 분리
    from sklearn.model_selection import train_test_split

    train_test_split(df_X, df_y, test_size = 0.2, shuffle = True, random_state = 2022, stratify = df_y)

    X_train.shape, X_test.shape
    ```

    ``` python
    # 학습
    from sklearn import svm #서포트 벡터

    svm.SVC(kernel = 'linear')#linear로 선형벡터 지정
    ```

    ``` python

    ```

4. 의사결정나무  
Node와 Leaf로 구성되어있다. 제일 위의 노드가 Root node라고 하는데 제일 위에서 제일 밑까지의 길이가 depth라고 한다. 위의 노드일수록 가장 넓은 범위를 묻고 내려갈수록 범위를 좁혀가야 학습이 된다. 이것은 스케일링을 하지 않아도 된다. 좌표를 통한 거리를 구하지 않아도 되기 때문이다. 인코딩 또한 안해도 된다. 앞서 했던 선형분리를 이진분류이다. 선을 이용해서 다중분류를 하기 위해서는 선을 3개를 구해야 하고 그 이후의 과정이 추가된다. 그러나 트리가 요즘 좋다 .약한 분류기인 디시젼 트리를 여러개 사용하는 것이 앙상블이라는 방법인데 이것이 강력하고 요즘 트렌드들도 트리 기반이다. 

5. 나이브 베이즈  
스팸메일을 분류하는 것을 예로 들어보자. 스팸메일 내부에서 상대적으로 얻어내기 쉬운 것들을 쓰면 알고자 하는 확률을 알 수 있다. 


6. 앙상블  
앙상블은 voting, bagging, boosting 세가지 방법으로 나뉜다. 보팅은 똑같은 데이터를 각가 다른 알고리즘에 집어넣어서 다수의 결과를 얻는 것이다. 베깅은 데이터를 여러 서브셋으로 나누고 같은 분류기로 결과를 만들어낸다. 트리로 배깅을 하는 것이 랜덤포레스트이다. 부스팅은 앞의 분류기를 돌리고 그 결과를 보고 그것을 보완하는 약한 분류기에 넣고 하는 연쇄적인 과정이다. 