# Numpy 설명

[넘파이 수업링크](https://velog.io/@mingki/Numpy-%EB%84%98%ED%8C%8C%EC%9D%B4)

1. 가상환경 구축  
C:workspace/myml 폴더를 만든 후 그 안에서 cmd창을 켜서 다음의 명령어를 실행한다.

    ```shell
    conda create -n myml python==3.8
    #만약 여기서 오류가 생긴다면 내 PC에서 PATH를 추가해주어야한다.

    conda install numpy

    conda activate myml

    pip install ipykernel

    python -m ipykernel intsall myml

    
    ```

2. 
``` python
import numpy as np

score = [12, 34, 56]

for i, s in enumerate(score):
    #기존의 리스트는 시간이 많이 걸린다. 그래서 넘파이를 이용해서 루프를 안쓰고 요소 하나하나에 대한 작업을 할 수 있는게 넘파이 이다.
        score[i] = s + 3
```

``` python
a = [10]
type(a) #list

x = (10)
type(x) #int 따라서 컴마를 찍어야 튜플 자료형이 된다.

x = (10,)
type(x) #tuple
```

3. ndarray 클래스  
차원이 여러개 있는 array를 다루는 클래스이다. 

    ``` python
    xarr = np.array([])

    print(xarr)

    xarr
    numpy.ndarray
    
    xarr.shape
    #(4,)

    x.dtype
    #dtype('int32')
    #데이터 타입으로 int32, int64, float32, float64의 형태를 많이 쓴다.

    ```

    ``` python
    # 2차원 리스트
    yarr = np.array([[10, 11], [12, 13]])
    yarr.shape
    #(2, 2)
    ```
    ``` python
    # 3차원 리스트
    yarr = np.array([[[1,2], [3,4]], [[5,6],[7,8]], [[9,10],[11,12]]])
    yarr.shape
    #(3, 2, 2) 2개짜리 리스트가 2개씩 묶여 3 묶음이 있다.
    yarr = yarr.astype('float32')
    #astpye은 숫자형식을 바꾸는 것인데 할당을 해야 원본이 변경된다.

    xarr = np.array([23., 45., 56., 76.])
    xarr.dtype
    #dtype('float64')

    xarr = np.array([23, 45, 56, 76], dtype = 'float64')
    xarr.dtype
    #dtype('float64')

    yarr = yarr.reshape(1, 3, 2, 2) #차원을 바꿔주는 함수이다.
    yarr.shape 
    #(1, 3, 2, 2)

    yarr.reshape(-1,2,2).shape #-1의 역할은 reshape함수가 차원을 계산해서 알아서 할당하는 자리이다. 지금까지 12개의 것을 다뤘기 때문에 위와 같이 하면 -1 자리에 3이 들어가게 된다. 따라서 위의 결과, shape은 (3, 2, 2)가 된다.

    yarr.flatten()
    yarr.reshape(-1)
    #이 2가지 방법을 통해 쭉 원벡터로 만들 수 있다.
    #array([ 1.,  2.,  3.,  4.,  5.,  6.,  7.,  8.,  9., 10., 11., 12.],dtype=float32)

    yarr[np.newaxis, :].shape
    #축을 맨 앞에 하나 추가할 수 있는 문법이다.
    #(1, 3, 2, 2)

    np.arange(10) #numpy array를 만들어주는 함수
    #[0,1,2,3,4,5,6,7,8,9]

    np.linspace(0, 10, 8) # 0에서 10사이를 8개로 나누라는 의미이다.
    #array([ 0.        ,  1.42857143,  2.85714286,  4.28571429,  5.71428571, 7.14285714,  8.57142857, 10.        ])

    np.full((2,3), 0) #하나의 숫자로 해당 차원의 어레이를 채우고 싶을 때 사용하는 함수
    np.zeros((2,3)) #같은 기능을 수행한다.
    #array([[0, 0, 0],[0, 0, 0]])
    np.zeros_like(yarr) #yarr과 같은 shape을 가지는 0으로 채워진 array를 만들어낸다.
    ```
4. Random(난수)
    ``` python
    np.random.uniform(0,10,5) #.uniform은 0, 10까지 동일한 확률로 뽑을 수 있을 때 랜덤으로 수를 하나 뽑아주는 함수이다. 괄호 안에 마지막 수는 그 수만큼을 뽑고 어레이로 만들어준다.
    np.random.normal(0,10,4) #.normal은 (0,10)의 정규분포에서 난수를 뽑아주는 함수이다.
    np.random.randn(2, 3) # (0,1)의 표준정규분포에서 (2,3)의 난수 어레이를 뽑아주는 함수이다.
    ```

5. 함수  
함수와 메소드의 차이가 무엇일까? 메소드는 클래스 아래에 있는 함수를 의미힌다. 


    ``` python
    arr = np.arange(0, 12).reshape(3, 4)
    xarr
    #array([[ 0,  1,  2,  3],[ 4,  5,  6,  7],[ 8,  9, 10, 11]])
    xarr.shape
    #(3, 4)
    xarr.sum()
    #66
    xarr.sum(axis=0)
    #axis를 지정하면 축에 해당되는 요소들만 더해진다.
    np.sum(xarr, axis=1) #위와 같은 역할을 한다.

    xarr.mean(axis=1)
    #axis에 해당하는 요소들의 평균을 구해준다.

    xarr.min(axis=0)
    #최솟값ㅇ를 구하는 함수

    xarr + [3]
    # 넘파이어레이의 연산자는 브로드캐스팅 해주는 것이다. 즉, [3]이 내부적으로 같은 크기로 바뀌어 다 더해진다.  
    # array([[ 3,  4,  5,  6],[ 7,  8,  9, 10],[11, 12, 13, 14]])

    x = np.array([[1, 2], [3, 4]])
    y = np.array([[1, 2], [3, 4]])
    x * y #그냥 곱
    #array([[ 1,  4],[ 9, 16]])
    x@y #매트릭스 곱
    #array([[ 7, 10],[15, 22]])

    x = np.array([1, 2, 3])
    y = np.array([1, 2, 3])
    np.dot(x, y) #같은 위치에 있는 것끼리 더한다.
    #14

    x = np.array([[1, 2], [3, 4]])
    y = np.array([[1, 2], [3, 4]])
    np.dot(x, y)#2차원 이상부터는 행렬곱으로 계산된다.
    #array([[ 7, 10],[15, 22]])

    np.matmul(x, y) #행렬 곱만 하는 함수
    #array([[ 7, 10],[15, 22]])

    x = np.array([1,4,3,2])
    x > 2 #요소 하나하나에 대한 결과를 반환한다.
    #array([False, False,  True])
    x[[False,  True,  True, False]] # 결과값을 리스트로 넣으면 True값만 반환되어 어레이로 나온다.
    # 이 과정을 함축한 것은 다음과 같다.
    x[x>2]

    x[x>2] = -1 # 나중에 위상치를 할 때 사용하는 것인데 2보다 큰 값을 해당 숫자로 치환할 수 있다.

    np.vstack((x, y)) #데이터를 아래로 붙이는 함수
    #array([[1, 2, 3],[4, 5, 6]])
    np.hstack((x, y)) #데이터를 옆으로 붙이는 함수
    #array([1, 2, 3, 4, 5, 6])

    np.concatenate((x,y), axis=1) # 축을 지정해서 데이터를 붙이는 함수이다. 

    ```

6. 인덱싱

    ``` python
    x=[[1,2],[3,4]]
    print(x[1][0])
    # 3

    x = np.array([[1,2],[3,4]])
    x[1, 0] #[열, 줄]
    # 3

    x = np.array([1, 2, 3, 4, 5])
    np.where(x>3) # where를 통해서 연산이 True인 인덱스를 반환한다. 
    # (array([3, 4], dtype=int64),)
    np.where(x>3, 1, 0) # 3보다 크면 1, 작으면 0으로 하라는 것

    #아래와 같이 함으로써 갯수를 셀 때 용이하다.
    x = np.array([1, 2, 3, 4, 5, 6])
    x = np.where(x>3, 1, 0)
    x.sum()
    

    x = np.random.randn(4, 3)
    x
    '''
    array([[ 0.13362409, -0.04302081, -1.63632672],
       [ 0.81197032,  0.75242425,  2.47210172],
       [ 0.77275609,  0.58676206, -1.46553777],
       [-2.20819645,  0.716572  , -1.10846267]])
    '''
    x = np.argmax(x, axis=1) #리스트 안에서 가장 큰 값을 반환한다. 딥러닝을 할 때 가장 높은 확률을 뽑을 때 잘 사용한다.
    #array([0, 2, 0, 1], dtype=int64)


    ```

7. 슬라이싱

    ``` python
    xarr = np.array([1, 2, 3, 4, 5, 6, 7])
    xarr[0:5]
    #array([1, 2, 3, 4, 5])
    xarr[:-1]#마지막 값만 빼고 만들 때 하는 슬라이싱
    #array([1, 2, 3, 4, 5])

    xarr = np.array([1, 2, 3, 4, 5, 6, 7])
    y = xarr[3:5]
    y[0] = -1
    y
    #array([-1,  5]
    x
    #array([ 1,  2,  3, -1,  5,  6,  7])
    # 끌어쓰면 원본이 조작된다.

    y = xarr[3:5].copy()
    #이런식으로 하면 원본 데이터가 변하지 않게 편집할 수 있다.
    ```

8. csv파일을 불러오기
    ``` python
    #현재 디렉토리 안의 datasets폴더의 파일을 읽어오는 함수이다. NDarray의 경우 리스트 안의 type이 일치되어야 오류가 일어나지 않는다. 아래의 코드를 실행한 결과도 문자열을 제대로 가져오지 못했다.
    iris = np.genfromtxt('./datasets/iris.csv', delimiter=',', skip_header=1)
    iris[:5]

    xarr = iris[:,:-1] #뒤에 이상한 부분을 제외하고 가져오는 코딩
    xarr

    m = 5.8 # m값을 기준으로 두 덩이를 나누는 방법
    x = xarr[xarr[:, 0] > 5.8, :]
    y = xarr[xarr[:, 0] < 5.8, :]
    x[:, 0].min()
    #5.9
    y[:, 0].max()
    # 5.7


    ```
9. 데이터를 파일로 저장하고 다시 열기
    ``` python
    np.savez('my_iris.npz', my_x=x, my_y=y) #npz 확장자로 저장하며, 앞서 만들었던 어레이를 키를 지정해서 저장할 수 있다.

    #파일을 불러오는 명령이다.
    my_iris = np.load('my_iris.npz')
    xarr = my_iris['my_x'] #키를 기억하고 불러와야 한다.
    type(xarr)
    #numpy.ndarray
    ```

