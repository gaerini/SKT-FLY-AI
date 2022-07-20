# Machine Learning Day1

1. 분류 알고리즘  

    * k-Nearest Neighbor(k-NN)  
    데이터를 분류하고 좌표평면에 배치한 후 새로운 데이터를 좌표에 배치했을때 어느쪽으로 분류되는지 위치하는 곳에 가장 가까운 것과 같은 종류라고 판단하는 방법이다. k의 의미는 판단에 사용할 가까운 이웃의 개수이다. k는 사용자가 지정해야한다.  

    * 거리 계산 방법
    보통 좌표평면에서 거리를 구하는 공힉은 유클리드 거리 방법이다. 이 방법으로 안돌아가는 알고리즘에는 멘하탄 거리 방법을 사용해야한다. 맨하탄 거리는 두 점의 x좌표 차와 y좌표 차를 더해서 구하는 방법이다.  

    * Norm  
    벡터의 길이, 혹은 크기를 측정하는 방법이다.  

    * Y가 연속형인 k-NN  
    새로운 데이터가 들어왔을 때 그 주변의 데이터의 평균을 이용해서 판단을 한다.  

    * k-NN Hyper-Parameter
     k값을 의미한다. k=1인 경우 가장 가까이 있는 것 하나만 보는건데 과대적합이 발생할 수 있다. 그러나 k가 커지면 과소적합이 생길 수 있다. 즉 k만 잘 찾으면 된다.  

     * k를 잘 구하는 방법  
    학습데이터와 검증데이터로 학습시킨 결과가 벌어지는 시작점, 혹은 학습 에러가 반등하는 지점에서 k를 결정해야한다.  

    * k-NN 실습  

        ``` python
        # 사이킷런 설치
        !pip install scikit-learn
        import sklearn
        sklearn.__version__
        ```

        ``` python
        #데이터 불러오기
        citrus = pd.read_csv('./datasets/citrus.csv')
        pd.DataFrame(citrus)
        citrus.shape
        ```

        ``` python
        # 불러온 데이터 확인
        citrus['name'].unique()
        citrus.info()
        citrus.isna().sum(axis=0) #결측치 없음
        citrus[citrus.duplicated()] #중복데이터 확인
        citrus['name'].value_counts() #name을 구성하는 데이터 확인
        sns.displot(data=citrus, x='diameter', hue='name', kind = 'kde') # 그래프로 분포 확인
        ```

        ``` python
        #인코딩
        
        from sklearn.preprocessing import LabelEncoder #사이킷런에서 제공하는 방법을 이용하여 인코딩을 진행할 수 있다.
        le = LabelEncoder()

        le.fit(df['name']) # 사이킷런에서는 fit하는 과정이 반드시 필요하다.

        df['name'] = le.transform(df['name']) # 핏을 한 후 transform을 하면 인코딩이 진행된다.

        df['name'] = le.fit_transform(df['name']) #fit과 transform 과정을 전부 할 수 있는 과정이다.

        le.classes_ # 인코딩의 결과를 알 수 있다. 0, 1 의 순으로 되기 때문에 순서대로 읽으면 된다.


        ```

        ``` python
        # 데이터 분리(학습/테스트 데이터)
        
        # X, Y 분리(독립변수와 종속변수를 분리)
        X = df.iloc[:, 1:]
        y = df.iloc[:, 0]

        #학습/테스트 분리(80:20)

        ## 셔플
        X, y = sklearn.utils.shuffle(X, y)

        ##셔플 후 슬라이싱
        idx = int(df.shape[0] * 0.8)

        X_train = X.iloc[:idx, :]
        X_test = X.iloc[idx:, :]

        y_train = y[:idx]
        y_test = y[idx:]

        # 위 두 방법을 한꺼번에 하는 방법을 자주쓴다.
        from sklearn.model_selection import train_test_split

        x_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=2022, stratify = y, shuffle = True)


        # 스케일링
        from sklearn.preprocessing import StandardScaler

        ss = StandardScaler()
        ss.fit(X_train)

        X_train_scaled = ss.transform(X_train)

        # 모델 학습
        from sklearn.neighbors import KNeighborsClassifier

        clf = KNeighborsClassifier()
        clf.fit(X_train, y_train)

        # 테스트
        X_test_scaled = ss.transform(X_test)
        X_test_scaled[:5]
        y_pred = clf.predict(X_test_scaled)
        (y_pred==y_test).sum()/X_test.shape[0] #정확도 계산

        #평가하기
        from sklearn.metrics import confusion_matrix

        cfm = confusion_matrix(y_test, y_pred)
        cfm

        #히트맵 그리기
        import matplotlib.pyplot as plt
        import seaborn as sns

        plt.figure(figsize=(6, 4))
        sns.heatmap(cfm, annot=True, fmt='g', cbar = False)
        plt.show()


        ```
2. support vector machine

선형 분류에 가장 알맞은 알고리즘이다. 비선형도 분류 가능하다. 이것이 하는 일은 데이터 군집을 가르는 무한대의 직선 중 가장 좋은 직선을 찾는 것이다. 같은 기울기로 선을 평행이동 했을 때 두 데이터에 닿는 마진을 찾고 그 마진 영역이 가장 넓은 것이 좋은 선이 있는 영역이다. 즉 벡터를 찾는 것이다. 마진에는 허용 범위가 전혀 없는 타이트한 하드 마진이 있고 에러를 조금 인정하면서 영역이 최대가 되게 하는 것이 소프트 마진이라고 한다. 우리는 대부분 소프트 마진으로 사용한다. 

비선형 분류는 선형 분류가 안되는 데이터 유형이 존재한다. 이런 종류는 차원을 확장하여 데이터의 분류 기준이 되는 평면을 찾을 수 있다. 그때 차원을 확장하는 방법을 kernel이라고 한다. 

