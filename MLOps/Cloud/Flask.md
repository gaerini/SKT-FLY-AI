# Flask
[Flask 실습 자료1](https://helloailab.notion.site/Flask-1-64d20b786ed94e62b93ebc38518eac41)

[Flask 실습 자료2](https://helloailab.notion.site/Flask-2-0c755ccea6194b7f9abf768d52bb206b)
## Definition
<hr/>
serving 할 수 있는 툴은 많다. 그 중에 우리는 Flask를 사용할 것이다.

Flask는 python 기반의 web framework에서 가벼운 축에 속한다.

* MVC 패턴
flask는 mvc 패턴을 따른다. model, view, controller

## Flask 설치
<hr/>  

``` bash
#디렉토리 생성
mkdir flask-tutorial
cd flask-tutorial

#Flask 설치
pip install -U Flask==2.0.2

#Flask 버전 확인
flask --version
```

## flask로 web server 띄우기
app.py를 다음의 내용으로 작성한다.
``` python
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

if __name__ == "__main__":
	app.run(debug=True, host='0.0.0.0', port=5000)
# debug 모드로 실행, 모든 IP 에서 접근 허용, 5000 포트로 사용하는 것을 의미
```

## Routing
<hr/>  

flask의 route()는 python함수를 web server의 URI에 매핑 시킬 수 있습니다.  
우리는 app.py를 다음과 같이 수정해봅시다.  

``` bash
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/helloai")
def hello_AI():
    return "<p>Hello, AI!</p>"

if __name__ == "__main__":
	app.run(debug=True, host='0.0.0.0', port=5000)
```
app.py를 실행하고 127.0.0.1:5000 으로 접속하면 Hello, World! 라는 문자가, 127.0.0.1:5000/helloai/ 로 접속하면 Hello, AI! 라는 문자가 브라우저에 보이는 것을 확인할 수 있습니다.

## Post Method
<hr/>  
route()를 통해서 URI 뿐만이 아니라 Http method도 저장할 수 있습니다.
다음과 같이 app.py를 수정해봅시다.   

``` bash
from flask import Flask
import json

app = Flask(__name__)

@app.route("/predict", methods=["POST", "PUT"])
def inference():
    return json.dumps({'hello': 'world'}), 200 # http status code 를 200 으로 반환하는 것을 의미합니다.

if __name__ == "__main__":
	app.run(debug=True, host='0.0.0.0', port=5000)
```

app.py를 실행하여 서버를 띄우고 다른 창에서 curl을 수행하여 http 응답을 확인합니다.  
``` bash
curl -X POST http://127.0.0.1:5000/predict
# {"hello": "world"}

curl -X PUT http://127.0.0.1:5000/predict
# {"hello": "world"}

curl -X GET http://127.0.0.1:5000/predict
# <!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2 Final//EN">
# <title>405 Method Not Allowed</title>
# <h1>Method Not Allowed</h1>
# <p>The method is not allowed for the requested URL.</p>
```
post와 put만 허용했기 때문에 get은 405 error가 발생할 것입니다.

## ETC
<hr/>  

- 이외에도 Flask 는 Web Application 을 구동하기 위한 다양한 기능들을 내장하고 있습니다.  

- 하지만 저희는 Flask 의 모든 기능을 살펴보는 것이 목적이 아니라, 여러분의 머신러닝 모델을 API 서비스로 제공(서빙)할 때, Flask 를 사용하는 방법을 알아보는 것이 목적입니다.  

- 다음 시간에는 Flask 를 활용하여 간단한 머신러닝 모델을 서빙해보겠습니다.

## Flask 에서 사용할 모델 학습 및 저장
<hr/>
우리가 사용할 샘플 코드는 다음과 같다.  

``` python
import os
import pickle
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier#랜덤포레스트 분류기 사용
from sklearn.metrics import accuracy_score, classification_report#정확도를 따지는 것
from sklearn.model_selection import train_test_split

RANDOM_SEED = 1234 #학습을 하기 전에 데이터를 랜덤으로 섞는 것. 얼마나 강하게 섞을 것인지를 나타낸다.

# STEP 1) data load
data = load_iris()

# STEP 2) data split
X = data['data']
y = data['target']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3,
                                                    random_state=RANDOM_SEED)

# STEP 3) train model
model = RandomForestClassifier(n_estimators=300, random_state=RANDOM_SEED)
model.fit(X_train, y_train) #fit으로 학습

# STEP 4) evaluate model
print(f"Accuracy :  {accuracy_score(y_test, model.predict(X_test))}")
print(classification_report(y_test, model.predict(X_test)))

# STEP 5) save model to ./build/model.pkl
os.makedirs("./build", exist_ok=True)
pickle.dump(model, open('./build/model.pkl', 'wb'))
```

flask-tutorial 에 위의 소스코드를 train.py를 저장하고 실행한다.
``` bash
cd flask-tutorial

# 파이썬 버전을 확인합니다.
python -V

# requirements 를 설치합니다.
pip install scikit-learn==1.0

# 위의 코드를 복사 후 붙여넣습니다.
vi train.py

# 위의 코드를 실행시킵니다.
python train.py
```
결과는 다음과 같이 나온다.  
``` bash
Accuracy :  0.9555555555555556
              precision    recall  f1-score   support

           0       1.00      1.00      1.00        16
           1       0.94      0.94      0.94        17
           2       0.92      0.92      0.92        12

    accuracy                           0.96        45
   macro avg       0.95      0.95      0.95        45
weighted avg       0.96      0.96      0.96        45
```

현재 디렉토리를 전부 살펴보면 build가 생성된 것을 알 수 있다.
``` bash
ls -al
#결과
total 20
drwxrwxr-x  3 jimmy7335 jimmy7335 4096 Jun 30 00:23 .
drwxr-xr-x 12 jimmy7335 jimmy7335 4096 Jun 30 00:21 ..
-rw-rw-r--  1 jimmy7335 jimmy7335  293 Jun 29 08:01 app.py
drwxrwxr-x  2 jimmy7335 jimmy7335 4096 Jun 30 00:23 build
-rw-rw-r--  1 jimmy7335 jimmy7335  920 Jun 30 00:21 train.py

```
## Flask Server 구현
<hr/>  

앞서 만든 모델을 load 하여 API를 제공하는 flask를 만들어 본다.
샘플 코드는 다음과 같다.
``` python
import pickle

import numpy as np #numpy는 기존의 python 연산보다 훨씬 빠르다. 이 때 사용된는 것이 ndarray이다. 즉, 숫자와 배열을 다루는 패키지이다.
from flask import Flask, jsonify, request

# 지난 시간에 학습한 모델 파일을 불러옵니다.
model = pickle.load(open('./build/model.pkl', 'rb'))

# Flask Server 를 구현합니다.
app = Flask(__name__)


# POST /predict 라는 API 를 구현합니다.
@app.route('/predict', methods=['POST'])
def make_predict():
    # API Request Body 를 python dictionary object 로 변환합니다.
    request_body = request.get_json(force=True)

    # request body 를 model 의 형식에 맞게 변환합니다.
    X_test = [request_body['sepal_length'], request_body['sepal_width'],
              request_body['petal_length'], request_body['petal_width']]
    X_test = np.array(X_test)
    X_test = X_test.reshape(1, -1)#머신러닝에서 사용하는 데이터 모양을 다시 만들어주는 명령어이다.

    # model 의 predict 함수를 호출하여, prediction 값을 구합니다.
    y_test = model.predict(X_test)

    # prediction 값을 json 화합니다.
    response_body = jsonify(result=y_test.tolist())

    # predict 결과를 담아 API Response Body 를 return 합니다.
    return response_body


if __name__ == '__main__':
    app.run(port=5000, debug=True)
```
* json 표기방법
[출처](https://dololak.tistory.com/256)  
JSON 문법
자바 스크립트 언어에 익숙한 사람이라면 다음의 규칙은 매우 익숙할 것 입니다.  
JSON 객체는 중괄호 블록 "{", "}" 으로 표기합니다.  
JSON 배열은 대괄호 블록 "[", "]" 으로 표기합니다.  
속성(Key)과 값(Value) 쌍으로 이룹니다.  
속성과 값이 쌍을 이룰 때 콜론으로 구분하며 속성 : 값 형태로 표기합니다.  
속성은 쌍따옴표(")로 묶어 표기하며, 값은 자료형에 따라 표기 방법이 달라집니다. ex) "age" : 3  
속성이 여러개인 경우 ,(콤마)로 구분합니다.
```java
[
    {
         "name" : "kim",
         "age"  : 19,
         "isAgree" : true,
         "hobby" : null
    },
    {
         "name" : "lee",
         "age"  : 18,
         "isAgree" : false,
         "hobby" : "cycle"
    }
]
```
위에 있는 소스코드를 flask_server.py로 저장하고 실행한다.

그리고 새로운 창을 열어 다음의 코드를 입력하여 결과를 확인한다.
``` bash
curl -X POST -H "Content-Type:application/json" --data '{"sepal_length": 5.9, "sepal_width": 3.0, "petal_length": 5.1, "petal_width": 1.8}' http://localhost:5000/predict

# 결과로 {"result":[2]} 가 나온다.
# 0, 1, 2  중의 하나의 type 으로 classification 하게 됩니다.

```