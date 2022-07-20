# EDA  
딥러닝을 학습시키는 데이터가 어떻게 구성되어있는지를 전체적으로 살펴보는 과정을 뜻한다.

    ``` python
    tips = pd.read_csv("./datasets/tips.csv")
    tips.shape #모양 확인
    tips.head()
    tips.info()
    df = tips.copy()#카피를 통해서 원본을 손상시키지 않게 한다.
    

    df["time"].unique() #time에 어떤 요소 있는지 확인
    df["day"].unique()
    df.describe().T #숫자형 자료를 볼 수 있는 것 T는 좌우 클론 바꾸기이다.

    #별측치 확인
    df.isna().sum(axis=0) 

    #중복치 확인
    df.duplicated().sum()

    df[df.duplicated(keep=False)] # 중복된 2 결과를 도출

    df=df.drop_duplicates(keep='first') #중복된 결과 삭제
    df.shape

    #결측치 확인
    sns.heatmap(df.isna()) #결측치가 있는 곳에 하얀색 선이 그어진다.

    #산점도 확인
    sns.pairplot(df)

    #상관관계
    df.corr() #숫자가 1에 가까울 수록 상관관계가 크다. 이것을 히트맵에 보면 조금더 보기 좋다.
    sns.heatmap(df.corr())

    ```
* Kaggle competition에 있는 것을 가져와서 보면 좋다. 그 중에 강사님이 가져온 데이터를 살펴보도록 하자.  

    ``` python
    #결측치를 나타내는 히트맵 라이브러리
    import missingno as msnum
    msnum.matrix(df)

    #결측치 처리
    # 머신러닝의 분류 알고리즘에 집어 넣을것인데 분류기준에 영향을 받지 않는 것을 지우고 결측치를 처리한다.

    df = df.drop(["PassengerId", "Cabin"], axis=1) # Cabin의 결측치가 너무 많아서 날렸다.
    df.head()

    # Age 결측치 처리
    df[df['Age'].isna()]
    df.Name.str.extract("([A-Za-z]+)\.") #Mr. Ms. 등을 끊어 오는 것이다.
    df['Initial'].unique()
    '''결과
    array(['Mr', 'Mrs', 'Miss', 'Master', 'Don', 'Rev', 'Dr', 'Mme', 'Ms',
       'Major', 'Lady', 'Sir', 'Mlle', 'Col', 'Capt', 'Countess',
       'Jonkheer'], dtype=object) '''
    #이것을 분석해서 나이를 대충 연상할 수 있다.

    # 연상되는 나이의 호칭으로 바꿔준다.
    be = ['Mlle', 'Mme', 'Ms', 'Dr', 'Major', 'Lady', 'Countess', 'Johnkeer', 'Col', 'Rev', 'Capt', 'Sir', 'Don']
    ae = ['Miss', 'Mrs', 'Miss', 'Mr', 'Mr', 'Mrs', 'Mrs', 'Other', 'Other', 'Other', 'Mr', 'Mr', 'Mr']

    # replace함수를 이용하여 initial 칼럼을 바꾼다.
    df['Initial']=df['Initial'].replace(be, ae)
    df['Initial'].unique()

    # 호칭별 나이 평균을 구한다.
    am = round(df.groupby("Initial").Age.mean())

    #원핫 인코딩 진행
    x = pd.get_dummies(df["Embarked"])
    x.columns=['C', 'Q', 'S']
    x

    #인코딩 한 결과를 concat
    df = pd.concat([df, x], axis=1)
    df.head()

    # 필요없는 칼럼 지우기
    df = df.drop(['Embarked','Initial'], axis=1)
    df = df.drop('Name', axis=1)
    df.head()

    # 데이터 저장하기
    key_x = df.to_numpy() #숫자 데이터만을 어레이로 저장하는 것이다.
    np.savez('data.npz', my_x = key_x)

    # 잘 저장되었는지 로드 해보기
    my_titanic = np.load('data.npz')
    titanicArr = my_titanic['my_x']
    titanicArr
    ```


* 상관관계 참조 사진  
![상관관계](https://blog.kakaocdn.net/dn/cQRtNe/btqxGwNhR4N/gIP2FoilomKprUEVqEACu1/img.png)  
