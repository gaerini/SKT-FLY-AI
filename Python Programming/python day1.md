# Python Programming Day1

1. 파이썬 프로그래밍 개발환경  
<hr/>  

* 파이썬 버전은 3.x.x 이런 포맷으로 되어있다. 2.x.x와는 API가 전부 바뀌었기 때문에 서로간의 호환이 안된다. 3.x.x 끼리는 호환이 가능하다. 이들은 버그 수정 본의 최신판에 따라 버전이 올라간다.  

* jupyter notebook의 경우는 구현하기에 알맞다. 도커 이미지를 그대로 다운받아서 쓰기에도 용이하다.  

* 교수님은 vscode를 사용한다.  

* 되도록 최신 버전을 설치하고 add python path를 해야 pip 등 실행에 필요하다.  
      
* interpretor를 수행하는 언어는 bash, basic 등이 있다. 파이썬도 거의 interpretor의 역할을 하는 것이다. 파이썬과 C의 중간에 있는 것이 자바이다. 컴파일하는 프로그램은 실행을 자기 자신이 스스로 한다. 자바는 자바 버추얼 머신에서 컴파일한 코드를 excusion 하는 것이다. 파이썬은 .py로 끝난다. idle이 우리가 짠 프로그램을 line by line으로 읽으면서 수행한다.
  
* compling approach는 스스로 돌아가야하기 때문에 다 집어넣어야한다. .exe를 생성하면 스스로 돌아가는 것이 그 예이다. 이것을 static binding이라고 한다. 그 반대로 dynamic binding 이 있다. 인풋이 들어오면 순간 라이브러리를 가져와서 수행한다. 파이썬의 경우 pi.py라는 사이트에서 온라인으로 가져온다.  

* 에러를 그대로 긁어서 **구글에 친다**.  
  
* idle 파이썬 라이브러리를 업데이트 하기 위해 프로젝트를 시작하기 전에 pip install -upgrade pip를 한다.  
  
2. 변수와 자료형  
<hr/>  

* 어떤 언어라도 시작은 assignment statement이다. a = 3 같은 것 말이다. 두 번째는 if나 else로 시작하는 conditional statement 이다. 세 번째는 for나 while을 이용하는 반복문이다. 네 번째는 io statement이다. 프로그래밍 언어마다 조금 다르지만 앞의 세개는 거의 비슷하다.  
  
* 값을 저장하는 장소가 있어야한다. 그 장소를 우리는 **변수**라고 한다. 수학과는 달리 저장한다는 의미가 강하다. 정확하게는 값을 저장하는 메모리 공간에 대한 tag이다.  
  
* **변수 이름 = 값** 이런 형태가 할당문이다. 왼쪽에는 항상 variable, 오른쪽에는 값이 와야한다. python의 특징은 자료형을 선언하지 않아도 된다. 오른쪽에는 계산 결과라던지, 변수간의 계산 식이 할당될수 있다.
  
* 변수 이름을 지을 때 알파벳으로 시작하고 나머지는 알파벳, 숫자, 언더바 등을 이용하여 하는 것이 좋다. '-'는 쓰면 안된다. 연산자이기 때문이다. <span style ='color:grey'>네이버나 구글에 파이썬 네이밍에 대해 참조를 얻어도 좋다.</span> git에 가서 파이썬 프로그래밍에 대해 공부를 해보면 스타일이 닮아진다.  
  
* variable의 type은 언제 정해지냐면 assign 될 때 정해진다. 파이썬은 9가지의 자료형(int, float, complex, bool, str, list, tuple, set, dict)을 지원한다. mutable 자료형은 값을 변경할 수 있는 자료형(list, set, dict)이고 immutable 자료형은 값을 변경할 수 없는 자료형이다. 재료를 하나씩 꺼내서 확인할 수 있는 자료형을 iterable 자료형(list, set, tuple, dict)이라고 한다.  
  
* 문자열이라는 것은 immutable이다.  
    ``` python
    >>> a = "hala python!"
    >>> type(a) = str
    #type은 인풋의 자료형이 아닌 가르키는 객체의 자료형을 반환한는 함수이다.
    ```
* int(), float(), str() 등의 함수로 자료형을 변환할 수 있다.  

* expression = Term+/-Expression이다. 이 때 Term은 Term (*, /, **) expression이 될 수 있다. 따라서 Term만 덜렁 남는다면 a = 3 이 되는 것이다.  

* 수식의 우선 순위는 우리가 하는 산술과정과 동일하다.  
  
* 복합연산자를 적용할 수도 있다. <span style="color:red">되도록 사용하지 말자. 헷갈린다.</span>  

* input()함수는 리턴할 때 까지의 입력을 문자열로 변수에 할당하는 것이다. <span style="color:red">숫자도 집언허으면 변수에 str로 저장된다.</span>  
  
* variable과 str을 결합할 때 blank를 집어넣는다.
    ``` python
    input(age)
    print("내 나이는", age, "입니다.")
    #결과 : 내 나이는 20 입니다.
    ```

3. 기본 문자열과 입출력 처리  
<hr/>  
  
* 문자열은 sequence of characters로 연속된 문자들의 집합을 의미한다.  

* 파이썬은 유니코드(UTF-8)를 사용한다. 한 문자를 3-4바이트로 나타내는 것을 의미한다. 이 코드 테이블의 일부분이 ASCII 코드이다. 한글은 2바이트를 사용한다.  

* 여러 줄 문자열을 만들려면 \n을 이용하여 줄바꿈을 한다.  

*  문자열 메소드 split()
빈칸으로 구분된 문장이 들어왔을 때 단어로 분리해서 얻어내고 싶을 때 사용하는 함수이다. split()의 결과는 튜플이고 이 항목들을 assign해준다. str.split()의 형태이고 default값은 빈칸으로 구분한다. 구분자를 집어넣으면 구분자별로 분리해준다. 

    ``` python
    msg = "Life is too short"
    w1, w2, w3, w4 = msg.split()
    print(w1) = "Life"
    ```
  
* 문자열을 formatting 하기 위해 %d, %s 등을 이용하여 문자열을 넣고 싶은 자리에 원하는 형식으로 삽입할 수 있다. {}을 이용하여 format()함수를 통해서도 할 수 있다.
    ``` python
    >>> print("The light was {:10}".format('good'))
    The light was good######
    ```  


* 파일 입출력  
    - 파일 열기
        ``` python
        # 스크립트 파일이 존재하는 폴더에 파일이 존재할 때
        fp_r = open("in.txt", 'r')
        fp_w = open("out.txt", 'w')

        # 스크립트 파일이 존재하는 폴더와 다른 폴더에 존재할 때
        fp_r = open("C:\work\in.text", 'r')
        ```  
    - 파일 읽기  

        fp_r은 파일이 어디에 있는지 나타내는 오브젝트를 가리키고 있다. 따라서 다음과 같이 객체에서 정보를 얻을 수 있는 메소드를 사용할 수 있다.  

        ``` python
        fp_r.read() #파일 전체를 하나의 문자열로 읽기
        fp_r.readlines() #파일을 줄 단위로 읽어 각 줄을 문자열로 저장
        fp_r.readline() #파일의 한 줄만을 문자열로 저장한다. 다음 줄을 읽기 위해서는 이 커맨드를 반복해야한다.
        ```  
    - 파일 쓰기  
        ``` python
        fp_w.write(string)
        ```
    - 파일 닫기  
        ``` python
        fp_r = open("in.txt", 'r')
        # 파일 닫기
        fp_r.close()
        # read() 반복문이 종료되면 자동으로 close()를 해주는 with를 사용하는 커맨드는 다음과 같다.
        with fp_r = open("in.txt", 'r')
        fp_r.read()
        ```


