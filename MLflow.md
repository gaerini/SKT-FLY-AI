# MLflow

[MLflow 실습1 노션 링크](https://helloailab.notion.site/MLflow-1-bc47b9a1766b4f87ad45dfd8d02707ab)  
[MLflow 실습2 노션 링크](https://helloailab.notion.site/MLflow-2-baf494f147544ad491c89896209ec81a)

## ML Management
<hr/>

* Model 소스코드
* Evaluation Metric 결과
* 사용한 parameters
* Model.pkl 파일
* 학습에 사용한 data
* 데이터 전처리용 코드
*  전처리된 data  

## ML Properties
- 비슷한 작업이 반복적으로 일어난다.
- Dependency패키지들이 많으며, 버전관리가 어렵다.
- 사람 Dependency가 생긴다.
- 테스트하기 어렵다.
* 여러 툴 중 MLflow를 사용할 것이다.

## MLflow의 장점
1. 쉬운 설치
2. 쉬운 migration
3. 대시보드 제공
4. 다양한 Client API 제공
5. 등등

## MLflow 설치
* mlflow-tutorial 디렉토리 생성
``` bash
 mkdir mlflow-tutorial

 ls #디렉토리가 잘 생성되었는지 확인

 cd mlflow-tutorial #디렉토리 안으로 들어간다.

```
* MLflow 설치
``` bash
python3 -V #파이썬 버전 확인

pip install mlflow==1.20.2 #mlflow 설치
```
``` bash
#현재 환경에서 오류가 나서 다음의 명령어를 입력해서 아나콘다 패키지를 따로 설치한다.

#출처 : https://helloailab.notion.site/MLflow-1-bc47b9a1766b4f87ad45dfd8d02707ab

# download
wget https://repo.anaconda.com/archive/Anaconda3-2021.05-Linux-x86_64.sh

# start install process
sudo bash Anaconda3-2021.05-Linux-x86_64.sh

#이후 잘 깔렸는지 확인하기 위해 버전을 확인한다.
mlflow --version
```
``` bash
1. Downgrade the protobuf package to 3.20.x or lower.
#다음과 같은 오류가 발생했다면 아래의 코드를 입력하여 버전을 낮춰보자.
pip3 install --upgrade protobuf==3.20.0
```
* 가상머신의 보안인 NSG의 5000번의 인과 아웃을 허용하기 위해 다음의 작업을 수행한다. 
    * AZURE 가상머신 - 네트워킹 - 인바운드 포트 규칙 추가(포트 5500번으로) - 아웃바운드 포트 규칙 추가(포트 5500번으로) 

## MLflow Tracking Server 띄우기
* mlflow ui 명령어  
이 명령어를 통해 서버 주소가 나타나게 된다.
``` bash
mlflow ui
#결과
[2022-06-29 06:21:47 +0000] [441813] [INFO] Starting gunicorn 20.1.0
[2022-06-29 06:21:47 +0000] [441813] [INFO] Listening at: http://127.0.0.1:5000 (441813)
[2022-06-29 06:21:47 +0000] [441813] [INFO] Using worker: sync
[2022-06-29 06:21:47 +0000] [441815] [INFO] Booting worker with pid: 441815
```
다음 명령어로도 서버 홈페이지에 접속할 수 있다.
``` bash
mlflow ui -h 0.0.0.0 -p 5000
```
이 상태로 다른 터미널을 한 개 더 열어서 동일한 디렉토리로 이동한 후 mlruns라는 디렉토리가 생성되었는지 확인한다.
``` bash
cd mlflow-tutorial
ls
cd mlruns
cat 0/meta.yaml
# 그 결과 다음과 같은 것이 나온다.
artifact_location: ./mlruns/0
experiment_id: '0'
lifecycle_stage: active #돌아가고 있다.
```
## sample code를 가져오기
다음의 명령어를 입력하여 다운 받는다.
```bash
pip install sklearn #사이킷런 설치

#자료 다운
wget https://raw.githubusercontent.com/mlflow/mlflow/master/examples/sklearn_elasticnet_diabetes/linux/train_diabetes.py
```

## Sample Code 실행
```bash
python3 train_diabetes.py
#결과
Elasticnet model (alpha=0.050000, l1_ratio=0.050000):
  RMSE: 78.59249466381223
  MAE: 66.30998032458166
  R2: 0.06607434687959957
Computing regularization path using the elastic net.
```
그 후 서버 페이지에 들어가면 리스트가 생성된 것을 알 수 있다.

* 다양한 parameter로 테스트
다음의 명령어를 하나씩 입력하면서 결과를 확인하자.
``` bash
python train_diabetes.py  0.01 0.01
python train_diabetes.py  0.01 0.75
python train_diabetes.py  0.01 1.0
python train_diabetes.py  0.05 1.0
python train_diabetes.py  0.05 0.01
python train_diabetes.py  0.5 0.8
python train_diabetes.py  0.8 1.0
```
* MAE, R2, RMSE
위 실행 결과에 나오는 세가지 값이다.
이 세가지의 값을 통해서 최고의 결과값을 채택한다.

