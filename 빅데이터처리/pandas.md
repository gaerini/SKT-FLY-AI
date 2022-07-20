# Pandas
기본적으로 엑셀을 생각하면 쉽다. 판다스가 가지고 있는 데이터의 형태는 feature가 column이 되게끔해야한다. row는 sample이라고 한다. (a, b)라는 자료는 샘플이 a개 특징이 b개라고 알면 된다.

1. 설치

    ``` shell
    pip pandas install
    ```
    ``` python
    import pandas as pd
    pd.__version__
    ```

2. pandas dataframe & series
판다스의 데이터프레임은 각각을 쪼개서 series로 다룰 수 있고 이것을 합쳐서 다룰 수 있다. 
![참조](https://blog.kakaocdn.net/dn/N4NAc/btqRoP1ml8o/x4DD7ITezrXVcJKgEYR5a1/img.png)
데이터 입장과 판다스 관점에서 명칭이 약간 차이가 존재한다.

    ``` python
    sr = pd.Series([3, 2, 2], name="apple")
    type(sr)
    #pandas.core.series.Series
    sr
    '''
    0   3
    1   2
    3   4
    4   7
    Name: apple dtype: int64
    '''

    sr2 = pd.Series([4, 5, 3, 4, 8], name='banana')
    sr3 = pd.Series([4, 5, 3, 4, 8], name='mango',index=['A','B','C','D','E'])

    df = pd.concat([sr, sr2], axis=1) #series를 붙여서 Dataframe을 만들 수 있다.
    type(df)
    #pandas.core.frame.DataFrame

    pd.concat([sr, sr3], axis=1)
    #인덱스가 다르기 때문에 길게 결합된다. 

    data = [
        ['John', 'Tom', 'Alice'],
        [3, 4, 5],
        [True, False, True]
    ]
    pd.DataFrame(data) #데이터 프레임을 형성해준다. 그러나 위의 결과는 우리가 원하는 형태로 나오지 않는다. 우리는 한 사람에 대한 데이터로 만들어야 한다. 
    #위의 내용을 그래도 쓰려면 아래와 같은 코드를 입력한다.

    data = [
        ['John', 3, True],
        ['Tom', 4, False],
        ['Alice', 5, True]
    ]

    #딕셔너리 형태로 쓰는게 명확하다.
    data = {
        'name':['John', 'Tom', 'Alice'],
        'point':[3, 5, 4],
        'Pass':[False, True, False]
    }
    df = pd.DataFrame(data)
    df.shape
    #(3, 3) 샘플 3개 피처 3개
    df.columns
    #Index(['name', 'point', 'Pass'], dtype = 'object')


    data = [
        ['John', 3, True],
        ['Tom', 4, False],
        ['Alice', 5, True]
    ]
    df_x = pd.DataFrame(data)
    df_x.columns = ['Name', 'Points', 'Pass'] #헤더를 입력해주는 것이다.

    #헤더 중 하나만 이름을 바꾸고 싶으면 다음과 같이 작성한다.
    df_x.rename(columns={'Point':'Score'})
    ```

3. 데이터 불러오기  

    ``` python
    iris = pd.read_csv("C:\workspace\myml\datasets\titanic.csv")
    iris.shape

    iris.head() #데이터가 어떻게 생겼는지 확인

    iris.info() #칼럼 이름, 자료형, 데이터가 들어있는 것이 몇개인지 등의 정보를 보여준다. 실제로 데이터가 nan이라고 써있을 수 있는데 이는 비어있는 데이터로 '별측치'라고 부른다. Dtype이 object이면 문자형이라는 뜻이다. 

    iris.isna() #na 즉, 비어있는지 알려주는데 비어있으면 True를 반환한다.
    sr = iris.isna().sum(axis=0) #각 컬럼마다 몇개가 비어있는지  카운팅해준다. 이것을 가지고 그래프를 그리면 된다.

    #별측치를 확인할 수 있는 그래프를 그려주는 그래프이다.
    import matplotlib.pyplot as plt
    plt.bar(sr.index, sr.values)
    plt.show()

4. 인코딩
문자로 되어있는것을 숫자로 바꾸는 작업을 의미한다. 단순하게 알파벳 순으로 숫자로 바꿀 수 있지만 머신러닝의 학습이 제대로 이루어지지 않을 가능성이 높아진다. 그래서 one hot 인코딩을 한다.  
A B O AB  
1 0 0 0  
0 1 0 0  
0 0 1 0  
0 0 0 1  

    이런식으로 하는게 one hot 인코딩이다. 이런 것은 순서가 없는 범주형 데이터에 적합하다. 학점에는 부적합하다.  

    ``` python
    #구성을 보여주는 함수
    titaninc["Embarked"].unique()
    titanic.Embarked.unique()

    #하나의 컬럼에 대한 원핫 인코딩을 실행시켜주는 함수
    pd.get_dummies(titanic["Embarked"])

    ```
5. 값 지정

    ``` python
    #여러개의 값을 지정하고 싶을 때
    titanic[["Embarked", "Pclass"]]
    #titainc["Embarked"]이런식으로 바로 부르면 시리즈로 불러오지만 위의 코드처럼 리스트로 감싸면 데이터프레임 형식으로 가져온다.

    #iloc을 이용하면 numpy와 비슷하게 특정 갯수를 가져올 수 있지만 조건을 넣기가 힘들다.
    titanic.iloc[0:5,0]

    #loc를 이용하면 조건을 지정하여 특정 요소를 가져올 수 있다.
    titanic.loc[titanic["Embarked"]=='C'& titanic['survived'] ==1, :]

    #인덱스로 소팅을 하는 방법이다. 데이터를 처리하다보면 데이터가 뒤죽박죽 되기 때문이다.
    titanic.sort_index(axis=0, ascending=False)

    #어떤 칼럼의 밸류로 소팅할지 정할 수 있다.
    pd.sort_values(by=["Age", "Fare"])
    ```

6. 칼럼 추가  
칼럼끼리 합치고 새로운 칼럼을 만들고 지우고 하는 feature engineering을 할 때 자주 사용한다.  

    ``` python
    #칼럼 추가
    titanic["FamilySize"] = titanic["SibSp"] + titanic["Parch"]

    #칼럼 삭제
    pd.drop(["SipSp", "Parch"], axis=1, inplace = True)
    #inplace = True는 원본을 바꿔주는 옵션이다.

    #어떤 조건에 맞는 칼럼을 가져와서 다른 값을 넣는 과정이다.
    titanic.loc[titanic["Age"] < 1.0, "Cabin"] = "None"

    #칼럼의 값 하나하나를 바꾸는 방법에는 2가지 방법이 있다.

    #1 특정한 타입을 값으로 가지는 칼럼을 가지고 오는 코드
    titanic.select_dtypes(include=["float64"])
    #칼럼의 최댓값과 최솟값의 차이를 반환하는 함수 정의
    def f1(x):
        #x의 type을 찍어보면 series가 나온다.
        return x.max() - x.min()
    #f1을 적용하여 다시 저장해주는 과정
    #df에 apply를 지정하면 series가 들어온다.
    df.apply(f1)

    #2
    def f2(x):
        # print(x)
        return x
    
    df["Age"].apply(f2) #시리즈가 들어오면 값이 들어오게 된다.

    #3 실제로 문자열을 값으로 가진 것을 숫자로 바꿀 때 다음 코드 처럼 값을 각각 바꿔줌으로써 해결할 수 있다.
    def f3(x):
        if x == 'male':
            return 1
        else:
            return 0
    
    titanic.Sex = titanic.Sex.apply(f3)
    titanic.head()

    #4 숫자값을 문자열로 바꿔보기
    titanic["Survived"]=titanic["Survived"].apply(lambda x :'saved' if x == 1 else 'lost')
    titanic.head()

    # map함수를 사용한 인코딩
    titanic["Survived"]=titanic["Survived"].map({"saved":0, "lost":1})
    titanic.head()

    #Nan 없애기
    titanic.dropna() # 하나라도 값이 없는게 있으면 없애버린다.

    #Nan에 0을 집어넣기
    x = titanic.fillna(0)
    x.head(10)

    #평균값을 구해서 Nan 치환하기
    titanic["Age"]=titanic["Age"].fillna(titanic["Age"].mean())
    titanic.isna().sum(axis=0)

    #대세에 지장없게 Nan의 값에 집어넣기
    titanic["Embarked"].value_counts() #Embarked 칼럼의 데이터 구성의 갯수를 알려주는 함수
    titanic["Embarked"]=titanic["Embarked"].fillna("S")
    titanic.isna().sum(axis=0)

    #특정 칼럼 삭제
    titanic.drop(["Cabin"], axis=1, inplace=True)
    ```

7. GroupBy  
Age 안에서 또 그룹을 묶어서 그 그룹의 평균 같은 것을 구하는 것이다.

    ``` python
    '''
        city	fruit	price	quantity
    0	Busan	Apple	100	    1
    1	Busan	Orange	200	    2
    2	Busan	Banana	250	    3
    3	Busan	Banana	300	    4
    4	Seoul	Apple	150	    5
    5	Seoul	Apple	200	    6
    6	Seoul	Banana	400	    7
    '''
    #city끼리 묶고 각 그룹별 price 평균을 구하는 과정
    df.groupby('city').price.mean()
    #city를 묶고 fruit 별 평균을 구하는 과정
    df.groupby(['city', 'fruit']).mean()
    ```

8. 연속형 데이터를 범주형으로 변경  
나이의 경우 연속적이라고 볼 수 있는데 나이대별 즉 10대, 20대로 나누는 과정을 의미한다.

    ``` python
    #Age 칼럼을 3등분으로 나눠서 첫번째를 child, 두번째를 young, 마지막을 old로 바꾸는 과정
    titanic["AgeClass"] = pd.cut(titanic['Age'], 3, labels = ['child', 'young', 'old'])
    titanic.head()

    titanic["AgeClass"].value_counts()
    ```
9. 문자열 처리

    ``` python
    data = {
        "Dave":"dave@gmail.com",
        "Steve":"steve@naver.com",
        "Rob":"rob@gmail.com",
        "Wes":"wes@hanmail.net"
    }

    sr = pd.Series(data)
    sr

    #시리즈 값의 문자열을 뭔가 하고 싶을 때 다음 코드를 사용한다.
    sr.str.contains("gmail") #어떤 문자를 포함되어있는 것을 반환
    sr.str.findall('^[a-zA-Z0-9+-\_.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$') # findall을 이용하여 정규표현식을 집어넣을 수 있다. 


    ```

10. 시계열 처리  
기계가 고장날 걸 알고 미리 셧다운 시킬 때 유용하게 사용했다. 판다스에서 이야기하는 시계열은 날짜데이터가 있는 것을 인덱스로 표현해서 나타낸 것이다.  

    ``` python
    data = np.random.randn(1000, 3)
    data.shape

    #시계열 데이터 형성하는 방법
    df = pd.DataFrame(data,
            index=pd.date_range('1/1/2022', periods=1000),
            columns = ['A', 'B', 'C'])
    
    ```