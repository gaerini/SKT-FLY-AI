# Python Programming Day3

1. Python Virtual Environment  
<hr/>  

* 왜 virtual environment가 필요한가?  
다른 버전이 필요한 프로젝트는 가상환경에서 호출하지 않으면 버전이 구분이 안되어 호출되기 때문에 버전의 구분이 필요한 경우 난처한 상황에 빠질 수 있다. 이는 같은 디렉토리에 저장되기 때문이다. 그래서 가상환경을 통해 격리된 환경을 만듬으로써 다른 환경의 영향에 구애받지 않고 잘 돌아가는 것을 보장받을 수 있게 된다.  

* Using Virtual Environment  
Python3 에는 가상머신을 만들 수 있는 venv가 있다.  

``` python
python -m venv env
```

system전체에 bcrypt가 설치되어있다. 그러나 가상환경에서 이것을 찾아보면 설치되어있지 않았다. 즉 격리되어있음을 알 수 있다.  

* Managing Virtual Environments-virtualenvwrapper  
- workon  
현재 있는 virtual environment가 몇개인지 알려준다.  
- cdvirtual.env  
원하는 virtual environment로 이동한다.  


* Pipenv: A New Python Packaging Tool  
가상 환경을 통해 의존성을 어느정도 해결했다. flask의 경우도 requirements.txt 파일을 통해서 의존성을 어느정도 해결한다. 이것을 pinning이라고 한다. 일반적인 해결책은 pip freeze를 사용해서 pinning을 수행한다. 그런데 만약 새로운 버전의 패치를 적용하면 어떻게 해야할까? static binding으올 만들면 되는 것이다. pipenv를 쓰는 것은 개발이 다 완료되고 맨 마지막 운영을 하기 전에 사용한다.  

* Pyinstaller  
배포완 관련된 것이다. 파이썬을 run하기 위해 .py를 사용해야한다. 범용성이 떨어진다. reader라는 폴더가 있다. 이것은 새로운 것이 변하면 그 리스트를 cli 터미널에 보여준다. 
