# Python Programming Day2
7. **함수, 모듈, 라이브러리 패키지** 
<hr/>  

* CS 에서의 함수는 수학의 함수와 같다. 수학에서는 결과값을 얻는 것을 목표로 했지만 프로그래밍에서는 꼭 그렇지만은 않다. 프로그래밍에서는 입력만 있고 행위만 하는 함수가 있기 때문이다.  

* 프로그램의 사이즈를 너무 길게하면 문제가 생길 수 있다. 함수를 사용하면 프로그래밍이 길어지는 것을 방지할 수 있다. 또한 자주 쓰는 것을 재사용함으로써 효율성을 높일 수 있다.  

* python에는 built-in 함수, 라이브러리 패키지 함수, user-defined 함수가 있다. 라이브러리 패키지의 경우, pi.py.org에서 가져온다. math, random, turtle 등이 있다. user defined 함수에서 라이브러리 패키지를 사용하고 싶으면 라이브러리 패키지 - 특정 써드파티 - user defined 순으로 import 하여 사용한다. 

* 패키지와 모듈의 차이점은 무엇일까? .py는 모듈이다. 다시 말해 메인 프로그램을 돌릴 수 있는, __main__가 있으면 모듈이라고 이야기한다. 단독으로 function을 테스트할 수 있는 것이다. 모듈의 set을 패키지라고 하는 것이다.  

* 사용자 정의 함수  

    - 사용자 정의 함수의 기본 형식  
        ```python
        def 함수이름 (매개변수1, 매개변수2, ...):
        statements
        return 값
        ```
    - 함수호출  
    반환값이 존재하지 않으면 함수만 작성함으로서 함수를 호출할 수 있지만 반환값이 있는 경우 변수에 assign을 해야 호출된다.  

    - call by keyword 형식  
    아래처럼 입력값을 변수에 지정하면서 직접적으로 대입함으로써 순서에 구애받지 않게 된다.

        ``` python
        def calc(x, y, z):
            return (x+y)*z
        sum = calc(z=30, x=10, y=20)
        print(sum)
        ```

    - call by reference 형식  
    어떤 나열된 수를 입력*튜플/리스트로 인식하여 입력받음으로서 처리하는것이다.  

        ``` python
        >>> def print_sum(*nums, sumfmt = "Sum is %d"):
            sum = 0
            for n in nums:
                sum += n
            print(sumfmt%sum)
        >>> print_sum()
        Sum is 0
        >>> print_sum(1,2,3,4,5)
        Sum is 15
        >>> print_sum(1,2,3,4,5, sumfmt = "전체 합은 %d 입니다.")
        전체 합은 15 입니다.
        >>>
        ```  

    - scoping  
    function 안에 들어가면 그 안의 variable은 영향을 받지 않는다.  

* 다양한 함수 사용  
    - map 함수  
    map을 하게 되면 단순히 시퀀스가 나오기 때문에 리스트를 만들고 싶으면 list()로 감싸야한다.  

    - filter 함수  
    filter 는 bool값이 리턴되기 때문에 true인 것만 실행하는 것이다.  

    - lambda 함수  
    함수의 인수로 함수를 넣어야할 때 사용하는 것이다. 보통 Lisp라는 프로그램에서 사용한다.  

        ``` python
        lst = [1, 2, 3, 4, 5]
        def square(n):
            return n*n
        lst2 = map(square, lst)
        sq_lst = list(lst2)
        print(sq_lst)

        #lambda 함수로 다음과 같이 사용할 수 있다.
        lst = [1, 2, 3, 4, 5]

        lst2 = map(lambda x: x*x, lst)
        sq_lst = list(lst2)
        print(sq_lst)
        ```

    - 재귀함수(recursive function)  
    함수 정의 안에서 자기 자신을 호출하는 것이다. 그 예로 팩토리얼 계산이 있다. 사실 상 recursion을 통해서 해결할 수 있는 것들이 상당히 많다. 

        ``` python
        def factorial(n):
            if n <= 1:
                return 1
            return n * factorial(n-1)
        ```  
* 지역변수와 전역변수  
    - global variable  
    프로그램 전체에서 사용할 수 있는 variable  

    - local variable  
    함수 내부에서만 사용할 수 있는 variable. <span style = "color:red">gloabal variable이 local variable과 충돌할시 local로 덮이게 되어있다.</span>  

    - 전역 변수 선언  

        ``` python
        def sub():
            global s #전역변수를 함수 안에서 변경하며 사용하려면 이렇게 선언해야한다. 
            print(s)
            s = "바나나가 좋음!"
            print(s)
        s = "사과가 좋음!"
        sub()
        print(s)
        ```  
* 라이브러리와 모듈  
    - 모듈  
    함수나 변수들을 모아놓으 파일. import를 사용해서 불러올 수 있다.  

    - 사용자 정의 모듈  
    같은 디렉토리에 .py파일이 존재하면 파일명을 import하여 그 안에 있는 함수 등을 불러올 수 있다.  

    - import 사용 방법  

        ``` python
        import 모듈이름 #모듈 내 모든 함수 사용가능
        import 모듈이름 as 줄임 #모듈 내 모든 함수이름을 줄여서 사용 가능
        from 모듈이름 import * #모듈 내 모든 함수 사용 가능
        from 모듈이름 import import 모듈함수 #지정된 함수만 사용가능
        ```  
8. **다양한 파일 입출력 처리**
<hr/>  

* CSV/Excel 파일 다루기  
    - CSV  
    컴마를 기준으로 나누어진 파일로 맨 윗줄은 각 데이터의 제목에 해당하는 헤더가 존재한다. 즉, 행으로 읽으면 하나의 튜플로 인식하여 처리할 수 있다. 엑셀로 csv 파일을 생성할 수 있고 공공기관에서 직접 파일을 받아올 수 있다. python에서 csv 라이브러리를 통해 읽을 수 있고 pandas를 이용해서 읽을 수 있다.  

* 한글 인코딩과 데이터 프레임  
    - 파일 처리시 한글 인코딩 문제  
    리눅스 환경에서는 한글이 안되는 경우가 있다. 그래서 파일에 저장하거나 읽을 때 인코딩 방식을 맞춰야한다.

        ``` python
        >>> f = open(한글테스트.txt, "r", encoding = 'utf-8')
        #cp949, euc-kr, utf-8 등으로 인코딩을 할 수 있기 때문에 위의 커맨드에서 바꿔주면 된다.
        >>> s = f.read()
        >>> print(s)
        This is text
        한글포함 문서
        >>> f.close()
        ```  

9. 객체지향 프로그래밍  
<hr/>  


* 객체  
    - 객체란 무엇인가?  
    객체란 어떤 속성과 행동을 가지고 있는 데이터를 말한다. 이미 우리는 String이라는 객체를 사용해보았다. 내용, 길이, encoding 등의 속성을 가지고 있고 대문자로 변경하거나 등등의 행동 또한 확인할 수 있기 때문에 객체라고 할 수 있다.  

    - 클래스  
    파이썬에서 제공하는 객체 외에 필요한 객체를 만들어서 사용할 수 있는데, 객체를 만들기 위해서는 클래스가 필요하다. 즉 객체를 찍어내는 틀이라고 생각할 수 있다.  

    - 클래스의 생성 방법  
    Rabbit이라는 이름의 클래스를 생성하여 토끼의 속성과 행동을 정의한 예는 다음과 같다.  
    
        ``` python
        class Rabbit :
            # 토끼의 속성(변수)
            shape = ""
            xPos = 0
            yPos = 0

            # 토끼의 행동(메소드)
            def goto(self, x, y):
                self.xPos = x
                self.yPos = y

        ```
        토끼 객체를  생성하기 위해서 다음과 같이 한다.  

        ``` python
        rabbit1 = Rabbit()
        rabbit2 = Rabbit()

        rabbit1.shape = "토끼"

        ```
* 특별한 메소드  
    - 생성자  
    객체를 생성하면서 변수의 값을 초기화하는 메소드이다. 생성자는 __init__() 의 형태를 가진다. 생성자를 통해서 생성을 할 때마다 실행시킬 것을 함수로 만들어 할 수 도 있다.

* 클래스의 상속  
    - 상속
    기존의 클래스가 가지고 있는 속성과 행동을 물려받아 새로운 클래스를 만드는 것. 토끼 클래스의 속성을 물려받아 집토끼 클래스와 산토끼 클래스를 만드는 것이 그 예이다. 이때 토끼 클래스를 슈퍼 클래스, 집토끼, 산토끼 클래스를 서브 클래스라고 말한다.  

    - 상속 구현  
        ``` python
        class 서브 클래스(슈퍼클래스):
            #서브 클래스 코드 구현
        ```

10. GUI Programming  
<hr/>  

* User Interface  
파이썬에서 프로그래밍을 사용하는 대부분의 사람들은 웹프로그래밍을 하지 않는다.  

11. Tkinter - the Python interface for Tk  
<hr/>  

* 개요  
Tkinter는 Tk 인터페이스의 약자로 Tk를 위한 파이썬 인터페이스이다. Tk는 widget을 만드는 것이 핵심이다. 즉 위젯이 object이다.

* Labels  
객체이기 때문에 아래와 같이 코딩할 수 있다.

    ``` python
    import tkinter as tk

    root = tk.Tk()

    w = tk.Label(root, text="Hello Tkinter!")
    w.pack()

    root.mainloop()

    ```
* message widget  
label과 유사하지만 글꼴도 변경할 수 있다.  

* buttons  
버튼을 누르면 click event가 일어났다고 알아야한다.  

    ``` python
    import tkinter as tk


    def write_slogan():
        print("Tkinter is easy to use!")

    root = tk.Tk()
    frame = tk.Frame(root)
    frame.pack()

    button = tk.Button(frame, 
                    text="QUIT", 
                    #fg= 'red',
                    command=quit)
    button.config(fg='red')
    button.pack(side=tk.LEFT)
    slogan = tk.Button(frame,
                    text="Hello",
                    command=write_slogan)
    slogan.pack(side=tk.LEFT)

    root.mainloop()

    ```  
* checkbox  

    ``` python
    from tkinter import *

    class Checkbar(Frame):
    def __init__(self, parent=None, picks=[], side=LEFT, anchor=W):
        Frame.__init__(self, parent)
        self.vars = []
        for pick in picks:
            var = IntVar()
            chk = Checkbutton(self, text=pick, variable=var)
            chk.pack(side=side, anchor=anchor, expand=YES)
            self.vars.append(var)
    def state(self):
        return map((lambda var: var.get()), self.vars)

      
    if __name__ == '__main__':
        root = Tk()
        lng = Checkbar(root, ['Python', 'Ruby', 'Perl', 'C++'])
        tgl = Checkbar(root, ['English','German'])
        lng.pack(side=TOP,  fill=X)
        tgl.pack(side=LEFT)
        lng.config(relief=GROOVE, bd=2)

   def allstates(): 
      print(list(lng.state()), list(tgl.state()))

   Button(root, text='Quit', command=root.quit).pack(side=RIGHT)
   Button(root, text='Peek', command=allstates).pack(side=RIGHT)
   root.mainloop()

    ```

    - if __name__ == “__main__”은 왜 필요할까?  
    __name__ 은 파이썬의 내장함수로, 모듈이 직접 실행될 때 그 모듈의 이름이 "__main__"이 되고 이것이 __name__의 값이 된다. 직접 실행되지 않는다면 모듈의 이름이 저장되어 있다. 따라서 위와 같은 조건문의 역할은 모듈이 직접 실행되고 있을 떼 조건 아래의 코드블럭이 실행되게 하는 것이다.  

* entry widgets  
사용자로부터 입력을 받는 역할을 한다. 다음은 예시이다.  

    ``` python
    import tkinter as tk

    def show_entry_fields():
        print("First Name: %s\nLast Name: %s" % (e1.get(), e2.get()))
        e1.delete(0, tk.END)
        e2.delete(0, tk.END)

    master = tk.Tk()
    tk.Label(master, text="First Name").grid(row=0)
    tk.Label(master,  text="Last Name").grid(row=1)

    e1 = tk.Entry(master)
    e2 = tk.Entry(master)
    e1.insert(10, "Miller")
    e2.insert(10, "Jill")

    e1.grid(row=0, column=1)
    e2.grid(row=1, column=1)

    tk.Button(master, 
            text='Quit', 
            command=master.quit).grid(row=3, 
                                        column=0, 
                                        sticky=tk.W, 
                                        pady=4)
    tk.Button(master, 
            text='Show', command=show_entry_fields).grid(row=3, 
                                                        column=1, 
                                                        sticky=tk.W, 
                                                        pady=4)

    master.mainloop()
    tk.mainloop()

    ```  

* canvas widget  
그래프와 그림을 그리게 해주는 위젯이다. 그래픽 객체 중에는 선, 원, 이미지 등이 있다. 아래는 그 예시이다.  

    ``` python
    # 사각형 안 사각형 만들기
    from tkinter import *

    master = Tk()

    w = Canvas(master, width=200, height=100)
    w.pack()

    w.create_rectangle(50, 20, 150, 80, fill="#476042")
    w.create_rectangle(65, 35, 135, 65, fill="yellow")
    w.create_line(0, 0, 50, 20, fill="#476042", width=3)
    w.create_line(0, 100, 50, 80, fill="#476042", width=3)
    w.create_line(150,20, 200, 0, fill="#476042", width=3)
    w.create_line(150, 80, 200, 100, fill="#476042", width=3)

    mainloop()
    ```  

    ``` python
    # canvas에 커서로 그림 그리기
    from tkinter import *

    canvas_width = 500
    canvas_height = 150

    def paint( event ):
        python_green = "#476042"
        x1, y1 = ( event.x - 1 ), ( event.y - 1 )
        x2, y2 = ( event.x + 1 ), ( event.y + 1 )
        w.create_oval( x1, y1, x2, y2, fill = python_green )

    master = Tk()
    master.title( "Painting using Ovals" )
    w = Canvas(master, 
            width=canvas_width, 
            height=canvas_height)
    w.pack(expand = YES, fill = BOTH)
    w.bind( "<B1-Motion>", paint )

    message = Label( master, text = "Press and Drag the mouse to draw" )
    message.pack( side = BOTTOM )
    
    mainloop()

    ```  

* sliders  
슬라이드하면서 수를 조종할 수 있는 위젯이다. 아래는 예시 중 하나이다.  

    ``` python
    from tkinter import *

    master = Tk()
    w = Scale(master, from_=0, to=42)
    w.pack()
    w = Scale(master, from_=0, to=200, orient=HORIZONTAL)
    w.pack()

    mainloop()

    ```  

* Textwidgets  
여러줄의 텍스트 영역을 제공하는 위젯이다. 예시는 아래와 같다.  

    ``` python
    import tkinter as tk

    root = tk.Tk()
    T = tk.Text(root, height=2, width=30)
    T.pack()
    T.insert(tk.END, "Just a text Widget\nin two lines\n")
    tk.mainloop()

    ```  

* Dialogs  
어떠한 대화 상자를 나타내주거나 경고, 오류를 출력해준다. 예시는 아래와 같다.  

    ``` python
    # 색깔 고르기 창 띄우기
    import tkinter as tk
    from tkinter.colorchooser import askcolor                  

    def callback():
        result = askcolor(color="#6A9662", 
                        title = "Bernd's Colour Chooser") 
        print(result)
    
    root = tk.Tk()
    tk.Button(root, 
            text='Choose Color', 
            fg="darkgreen", 
            command=callback).pack(side=tk.LEFT, padx=10)
    tk.Button(text='Quit', 
            command=root.quit,
            fg="red").pack(side=tk.LEFT, padx=10)
    tk.mainloop()

    ```

* Menu  
창의 상단에 메뉴바를 넣을 수 있다. 예시는 아래와 같다.  

    ``` python
    from tkinter import *
    from tkinter.filedialog import askopenfilename

    def NewFile():
        print("New File!")
        return
    def OpenFile():
        name = askopenfilename()
        print(name)
    def About():
        print("This is a simple example of a menu")
    
    root = Tk()
    menu = Menu(root)
    root.config(menu=menu)
    filemenu = Menu(menu)
    menu.add_cascade(label="File", menu=filemenu)
    filemenu.add_command(label="New", command=NewFile)
    filemenu.add_command(label="Open...", command=OpenFile)
    filemenu.add_separator()
    filemenu.add_command(label="Exit", command=root.quit)

    helpmenu = Menu(menu)
    menu.add_cascade(label="Help", menu=helpmenu)
    helpmenu.add_command(label="About...", command=About)

    mainloop()

    ```  

11. web programming with flask  
<hr/>  

* 개요  
    - web framework  
    하위 수준의 세부 사항에 대해 신경 쓰지 않고도 애플리케이션을 작성할 수 있도록 지원하는 라이브러리 및 모듈 모음

    - flask  
    파이썬으로 작성된 웹 애플리케이션 프레임워크. flexible하게 쓸 수 있지만 django보다는 stability가 떨어진다.  

    - WSGI  
    웹 서버와 웹 애플리케이션 사이의 범용 인터페이스를 위한 규격  

    - Werkzeug  
    요청, 응답 개체 및 기타 유틸리티 기능을 구현하는 WSGI 툴킷  

    - Jinja2  
    python용 템플릿 엔진이다.  

* 개발 환경 설정  
    ``` bash
    #가상환경 설치할 디렉토리 형성후 가상환경 설치
    mkdir envSKFLYAI
    cd envSKFLYAI
    python -m venv envSKFLYAI

    #가상환경 활성화
    envSKFLYAI\scripts\activate

    #flask를 가상환경에 설치
    pip install Flask
    ```

* hello.py 실행  
    ``` python
    from flask import Flask
    app = Flask(__name__)

    @app.route('/')
    #Flask 클래스의 route() 함수는 decorator로, 응용 프로그램에서 관련 함수를 호출하는 URL을 알려준다.
    def hello_world():
        return 'Hello World'
    if __name__ == '__main__':
        #Flask 클래스의 run() method는 로컬 개발 서버에서 애플리케이션을 실행
        app.run()

    ```  
    이것을 실행하게 되면 cmd창에 나타나는 주소를 복사해서 웹브라우저로 접속하면 Hello World가 출력되는 것을 확인할 수 있다.  

* Routing  
Flask의 route() decorator는 URL을 함수에 바인딩하는 데 사용한다. 괄호 안에 '/hello'를 입력하면 url 주소 뒤에 써서 접속할 수 있다. 







    


