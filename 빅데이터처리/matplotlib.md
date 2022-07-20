# Matplotlib  
[matplotlib 참조 링크](https://matplotlib.org/stable/api/index.html)  

우리가 그릴 수 있는 것은 매트플롯립을 다 그릴 수 있다. 그러나 이쁘게 그릴려면 코딩이 많기 때문에 신중하게 그리거나 보고서 등을 작성할 때는 seaborn이라는 라이브러리를 이용한다. 

1. matplotlib 설치
    ``` python
    !pip install matplotlib
    ```

2. 
    ``` python
    import matplotlib.pyplot as plt

    xarr = np.random.rand(15).

    #plot은 가장 기본 함수이다.
    plt.plot(xarr)
    plt.show()
    ```
3. 기억할만한 그림  
![참조](https://srishti.dev/img/axes_axis.png)
각 영역과 축에 대한 것, 범례 등을 잘 봐야 차트 그릴 때 헷갈리지 않는다.  
![참조2](https://actruce.com/wp-content/uploads/2020/05/anatomy.png)


4.  
    ``` python
    plt.figure(figsize=(4, 3)) #차트의 크기를 4인치, 3인치로 설정
    
    plt.figure()
    plt.subplot() # 내부적으로 축을 추가하는 함수
    plt.plot(xarr) # 이 함수는 위 두 과정을 내부적으로 자동으로 다 해준다. 세부적인 특징을 바꾸기 위해서는 명시를 각각 해주어야한다.
    plt.show()


    #플롯을 여러개 표시하는 방법
    plt.figure()
    plt.subplot(1,2,1) #밑으로 한개, 옆으로 2개를 그리겠다. 그중에 1번을 나타낸다.
    plt.subplot(1,2,1) #밑으로 한개, 옆으로 2개를 그리겠다. 그중에 2번을 나타낸다.

    #명시적으로 작성하는 방법
    fig = plt.figure()
    ax1 = fig.add_subplot(2, 2, 1)
    ax2 = fig.add_subplot(2, 2, 2)
    ax1.plot(xarr)
    ax2 = plot(yarr)


    # 미리 만들어놓고 그리는 법
    fig, axes = plt.subplots(2, 2) # 미리 4 칸이 만들어진다.
    axes[0, 0].plot(xarr) (0,0) 좌표의 칸에 그래프를 그린다.
    axes[1, 1].plot(yarr)
    plt.show()
    ```

    ``` python
    xarr = np.random.rand(15).cumsum()
    yarr = np.random.rand(15).cumsum()
    zarr = np.random.rand(15).cumsum()

    plt.figure(figsize=(8,6))
    plt.plot(xarr, label = "Korean", color = 'r')
    plt.plot(yarr, label = "English", color = 'g')
    plt.plot(zarr, label = "Japanese", color = 'b')
    plt.title("This is title")
    plt.xlabel("X label")
    plt.ylabel("Y label")
    plt.legend()
    plt.show() # 축 하나에 3개의 그래플가 그려진다.
    ```

5. 산점도
산점도를 사용하면 점들이 어떤식으로 모여있는지 확인할 수 있다. 

    ``` python
    plt.scatter(xarr, yarr)
    plt.show()
    ```

6. bar plot  
범주형 데이터를 나타낼 때 좋다.
    ``` python
    year = ['A', 'B', 'C']
    points = [100, 200, 300]
    plt.bar(year, points)
    plt.show()
    ```
7. 히스토그램

    ``` python
    points = np.random.normal(80, 10, 50)
    points plt.hist(points, '''bins = 20''') #기본은 10개로 쪼개짐
    plt.show()
    ```
8. BoxPlot

    ``` python
    x = np.random.normal(0, 2.0, 100)
    y = np.random.noraml(-3, 1.5, 500)
    z = np.random.normal(1.2, 1.5, 1000)
    ```

9. 이미지 삽입  

    ``` python
    import matplotlib.image as img

    img = plt.imread('./datasets/dog.jpg')
    type(img)

    plt.imshow(img)
    plt.xticks([]) #x축 삭제
    plt.yticks([]) #y축 삭제
    plt.show(img)

    ```