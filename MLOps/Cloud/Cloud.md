# Cloud Service

1. 클라우드 서비스 모델  
<hr/>  

공용 클라우드, 사설 클라우드, 하이브리드 클라우드  
하이브리드의 경우 프라이빗하게만 사용되다가 트래픽이 몰리면 공용이랑 같이 쓰이는 것이다.  
하이브리드 내부에서 공용과 사설을 잇는 것이 VPN 이다.  
ex) 수강신청  

2. 클라우드 서비스 유형  
<hr/>  
IaaS, PaaS, SaaS  

* Infrastructure - as - a -Service(IaaS)  
네트워크, 저장소, 서버를 클라우드 제공자가 관리  
셀프 서비스 포털을 통해 프로비저닝과 관리할 수 있는 컴퓨팅 인프라 제공  
이것이 가장 유연한 클라우드 서비스이지만 그만큼 모든 것을 관리해야한다.  


* Platform - as - a -Service(PaaS)  
IaaS에서 런타임과 미들웨어까지 제공하는 것을 의미한다.  

* SaaS  
PaaS에서 어플리케이션까지 제공하는 것이다.  

# Azure

1. region  
<hr/>  

고속 네트워크를 통해 연결된 데이터센터의 집합으로 전 세계적으로 66개 지역, 160개국에서 사용 가능하다. 

2. regional pair  
<hr/>  

지역끼리 쌍을 맺는다. 어떤 파일이 데이터 센터에 집어넣으면 이 파일에 대한 백업본을 2개 만든다.  
더 중요한 파일이라면 다른 데이터센터에도 백업본을 만든다. 

3. Azure Resource Manager
<hr/>  

Azure Portal, Azure PowerShell, Azure CLI, REST Client  
REST client가 필요한 이유는 어떠한 스크립트를 짠 것을 사용자들이 요청할 때마다 자동으로 돌려주기 위함이다. 

4. 용어 정리  
<hr/>  

리소스 : 가상 머신, 데이터 베이스, 가상 네트워크 등 단일 리소스를 나타내는 단위  
리소스 그룹 : 리소스를 묶을 수 있는 단위  
리소스 공급자 : 원하는 리소스를 제공하는 서비스  
리소스 제공자 : 리소스를 제공하는 주체  

5. Azure 계정  
<hr/>  

* 리소스 그룹 생성  
리소스 그룹 이름 : HelloAzure-RG  
영역은 Korea Central  
리소스가 많아지면 관리하기 어렵기 때문에 태그가 필요하다. 태그를 검색해서 쉽게 이용할 수 있다.  
태그 이름 : category  
태그 값 : showmethemoney  
구독 ID라는 것을 볼 수 있는데 전세계에서 유일한 ID로 구별자의 역할을 한다.  

* 리소스 만들기  
    - 공용 IP 주소 만들기  
    우리는 IPv4(4자리), 기본 SKU(스펙)를 사용할 것이다. 
    계층은 지역으로 한다. 주소 할당 중 동적은 시간이 지나면 주소가 바뀔 수 있는 것이고 정적은  바뀌지 않는 것이다. 위치는 asia pacific으로 하자.  
    이름은 HelloAzure-PIP  

* 포탈 창에 있는 cloud shell  
리눅스 기반의 콘솔창을 띄워주는데 웹 브라우저만 있으면 리눅스 창을 띄워준다.  
아이패드에서도 동일하게 사용할 수 있다.  
가장 많이 사용하는 명령어로 az 명령어가 있다. az --help를 이용해서 어떤 명령어를 사용할 수 있는지 확인해보자.  
이것 대신에 Azure CLI를 사용한다.

* 국내의 유명한 클라우드 서비스 프로바이더 회사  
메가존 클라우드, 베스핀글로벌

6. Azure power shell 실습  
<hr/>  

 * 계정에 대한 정보를 json 타입으로 출력  

         ``` bash
        az account list
        ```

 * 리소스 그룹 생성
    ``` bash
        #미국 서부에 생성하고 이름은 MyRG 이다. 
        az group create --location westus --name MyRG
        # 실행 결과
        {
        "id": "/subscriptions/c8733034-a0a1-45d7-abd1-3ad6f1821982/resourceGroups/MyRG",
         "location": "westus",
        "managedBy": null,
        "name": "MyRG",
        "properties": {
        "provisioningState": "Succeeded"
        },
        "tags": null,
        "type": "Microsoft.Resources/resourceGroups"
        }
    ```

* 가상머신 생성  
``` bash
    #location을 따로 지정하지 않아도 됐지만 기존의 리소스의 로케이션에서 되지가 않아 새롭게 korea central 로 로케이션을 변경했다.
    az vm create -n myVM -g MyRG --image UbuntuLTS --generate-ssh-keys --location koreacentral

    #결과
    It is recommended to use parameter "--public-ip-sku Standard" to create new VM with Standard public IP. Please note that the default public IP used for VM creation will be changed from Basic to Standard in the future.
    {
     "fqdns": "",
        "id": "/subscriptions/c8733034-a0a1-45d7-abd1-3ad6f1821982/resourceGroups/MyRG/providers/Microsoft.Compute/virtualMachines/myVM",
    "location": "koreacentral",
    "macAddress": "00-0D-3A-D7-06-3E",
    "powerState": "VM running",
    "privateIpAddress": "10.0.0.4",
    "publicIpAddress": "20.214.246.126",
    "resourceGroup": "MyRG",
    "zones": ""
    }
```

7. azure cli 다루기 
<hr/>  

* azure cli 설치  
    [azure cli 설치 링크](https://docs.microsoft.com/ko-kr/cli/azure/install-azure-cli-windows?tabs=azure-cli)  

* 로그인  
윈도우 cmd 창을 열어 다음의 커맨드를 입력하여 로그인한다.  
``` dos
az login
```
이제 여기서 작업하는 것이 연동되는 것이다.  

 * 버전 확인  
 ``` dos
az --version
 ```
* 계정 정보 확인  
 ``` dos
az account list
 ```

8. 가상머신의 크기를 조절하는 방법  
<hr/>  

- DB 다루기
    * scale up
    * scale down

* 컴퓨터 개수를 늘리는 것 - scale out  
* 컴퓨터 개수를 줄이는 것 - scale in 

9. 리소스와 리소스 그룹 관리  
<hr/>  

어떤 사람이 클라우드 계정을 사용하려고 할 때 구독과 연결되어있어야한다.  
구독에는 결제가 연결되어 있어야한다.  
그러면 구독 하나에 다른 사람을 연결해서 사용할 수 있을까?  
azure에는 디렉토리라는 개념이 들어간다. 여기서 말하는 디렉토리에는 사람들의 계정, 그룹 정보 등이 들 있다. 디렉토리에 구독을 붙일 수 있다면 다른 사람들이 사용할 수 있을 것이다. 그렇기 때문에 디렉토리에 대한 이해가 중요하다.  

10. 디렉토리 in azure  (Azure Active Directory)  
<hr/>  

전 셰계의 회사가 연결되는 것이다. 전부다 active directory에 달려 있는 형태이다. 허용을 해주면 디렉토리가 연결되는 것이다. 

# 인증과 권한  

1. Azure Active Directory(Azure AD)  
<hr/>  

다중 테넌트(각자 가지고 있는 디렉토리) 클라우드 기반 디렉터리 및 ID 관리. 테넌트에 구독이 붙는 것이다. 구독 하나가지고 여러개의 테넌트를 사용할 수 없다. 여러개의 테넌트를 쓰고 싶다면 구독을 더 해야한다. 

# Azure IaaS  

1. 네트워크   
클라우드에서는 하드웨어적인 L4기능은 없다. 다만 소프트웨어적으로 존재한다. 그것을 부하 분산기(load balance)라고 한다. 마찬가지로 옵션에 따라 방식을 바꿀 수 있다. 

2. IP address  
IPv4의 예시 : 20.18.16.100  
각 자리는 0~255 즉 256가지를 표현할 수 있고 2^8 즉 8비트 * 4 32비트 체계이다.  

3. subnet  
어떤 ip 주소를 가지고 라우터가 이를 내부 망과 연결시켜준다. 바깥 망은 public ip, 안쪽 망은 private ip이다. private ip 중 하나인 192.168.0.1이라고 하면 보통 1은 라우터가 가지고 있다. 1개의 라우터가 너무 많은 것을 처리할 수 없으니 네트워크를 끊어서 따로따로 사용하는 것이다. 이것을 subnet이라고 한다. cidr로 크기를 조정할 수 있다. 일부는 미리 정의되어있는  subnet도 존재한다. 

4. CIDR(Classes Inter-Domain Routing)  
서브넷을 라우팅하는 것을 의미한다. 일반 가정집에서는 ip 주소 하나를 받아서 내부 주소로 여러개 나눠쓰는 것이다. 일반 회사의 경우 203.100.111.xxx가 하나의 자리를 가지는 것이다. 각각의 자리수를 A, B, C 클래스이고 C 클래스를 예로 들면 255.255.255.0 이다. 이것을 'subnet mask'라고 한다. 즉, subnet mask와 같은 기능이지만 더 잘게 쪼갤 수 있ㄷ는 것이 차이점이다. 대제체적으로 12번을 이용해서 만든다. 즉 우리 집 컴퓨터에서 웹서버를 만들지 못한다. 

# Azure Virtual Network 실습  
1. 베스천  
클라우드 안에서 서비스가 되고 있는 것이 포탈인데 포탈 안에서 바로 서버로 접속할 수 있는 방법을 제공해준다. 마우스로 조종할 수 있다.  
2. DDos  
1G 통신선이 있을 때 수많은 컴퓨터가 요청을 할 때 마비가 되는 것이다. 그래서 정상적인 이용자가 정보를 열람하지 못하는 경우를 이야기한다.  
3. 방화벽  
침입하는 것을 보고 막아내는 하나의 컴퓨터.  
