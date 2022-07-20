# Seaborn

[seabornsite](https://seaborn.pydata.org)  

1. seaborn 설치  
    ``` python
    !pip install seaborn
    ```

2. 기본 임포트  

    ``` python
    import numpy as np
    import pandas as pd
    import matplotlib.pyplot as plt
    import seaborn as sns
    ```

3. 히스토그램

    ``` python
    plt.figure(figsize=(6,4)) # 사이즈 조정
    sns.histplot(data=titanic, x='Age') #Age를 x축으로
    plt.show()

    plt.figure(figsize=(6,4))
    sns.histplot(data=titanic, x='Age', bins = 8)#8개의 봉으로 쪼갠다.
    plt.show()

    plt.figure(figsize=(6,4))
    sns.histplot(data=titanic, x='Age', bins = 8, kde = True)#선 추가
    plt.show()

    plt.figure(figsize=(6,4))
    sns.histplot(data=titanic, x='Age', bins = 8, hue = 'Survived') #survived를 기준으로 나타내주는 것
    plt.show()
    ```

4. displot  
figure-level plot이라고 한다. 이것은 matplotlib의 설정이 먹지 않는다. seaborn의 API 문서를 참조하여 진행한다. 

    ``` python
    sns.displot(data=titanic, x='Age')
    plt.show()

    sns.displot(data=titanic, x='Age', kde=True)
    plt.show()

    # 막대를 없애는 옵션
    sns.displot(data=titanic, x='Age', kind = 'kde')
    plt.show()

    # 그래프를 2개 그리는 방법. survived를 기준으로 그린다.
    sns.displot(data=titanic, x='Age', col='Survived')
    plt.show()

    # hue 적용 가능
    sns.displot(data=titanic, x='Age', col='Survived', hue = 'Sex')
    plt.show()
    ```

5. 막대그래프  
x축이 범주형 데이터이고 그 count를 y에 하는 것  

    ``` python
    titanic["Pclass"].value_counts()

    # 각각의 데이터의 갯수를 구하고 그래프로 바로 보여주는 코드
    sns.countplot(data=titanic, x='Pclass')


    # 요금을 다 더해서 클래스가 상위 몇프로인지 알려주는 코드. 
    sns.barplot(x="Pclass", y='Fare', data = titanic)
    ```

6. point plot  
매트폴립에 있지 않은 그래프이다.  

    ``` python
    sns.pointplot(x='Pclass', y='Fare', hue='Sex', data=titanic)

    ```

7. Box plot  

    ``` python
    sns.boxplot(x='Pclass', y='Age', data=titanic, hue='Sex')
    ```

8. violin plot  

    ``` python
    sns.violinplot(x='Pclass', y='Age', data=titanic)

    #spit을 이용하여 hue를 반반으로 볼 수 있다.
    sns.violinplot(x='Pclass', y='Age', data=titanic, hue = 'Sex', split = True)


    ```

9. count plot  
사실상 가장 많이 쓰는 것. 몇 개인지 시각적으로 나타나기 때문이다.

    ``` python
    sns.countplot(x='Embarked', data=titanic)
    ```

10. 히트맵  

    ``` python
    sns.heatmap(data, annot = True) #큰 값을 가질 수록 밝은 색이다.

    sns.heatmap(data, annot = True, cmap="YlGnBu") #색깔을 바꿀 수 있다. cmap 종류는 구글링을 통해 얻을 수 있다.
    ```

11. scatter plot  

    ``` python
    tips = sns.load_dataset('tips')
    type(tips)

    tips.head()

    sns.scatterplot(x='total_bill', y='tip', data=tips)
    plt.show()

    #선형 회귀를 하기전 선을 시각적으로 찾을 수 있다.
    sns.regplot(x='total_bill', y='tip', data=tips)
    plt.show()
    ```

12. pair plot  
어떤 속성과 어떤 속성이 어떤 관계를 가지는지 개략적으로 판단할 수 있는 그래프를 제공한다.

    ``` python
    df = sns.load_dataset('penguins')
    df.head()

    sns.pairplot(df)
    ```
