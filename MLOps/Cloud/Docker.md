# Docker
[Docker1 링크](https://helloailab.notion.site/Docker-1-bb3017bde7284a3ea3b0e06ec2639d79)

## Docker 설치
<hr/>  
패키지 매니저를 업데이트 합니다.  

``` bash
sudo apt-get update
sudo apt-get upgrade
```

docker의 prerequisite package를 설치합니다.  
``` bash
sudo apt-get install \
    apt-transport-https \
    ca-certificates \
    curl \
    gnupg \
    lsb-release
```

docker의 GPG key를 추가합니다.  
``` bash
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg
```

stable 버전의 repository를 바라보도록 설정합니다.  
``` bash
echo \
  "deb [arch=amd64 signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu \
  $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

#arm 기반의 cpu는 아래의 코드를 입력합니다.
echo \
  "deb [arch=arm64 signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu \
  $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
```

Docker 엔진을 설치합니다.  
``` bash
sudo apt-get update
sudo apt-get install docker-ce docker-ce-cli containerd.io
```

정상적으로 설치되었는지 확인해보기 위해 다음 명령어를 입력합니다.  
``` bash
sudo docker run hello-world


#정상 설치되었다면 다음과 같은 결과가 나올 것입니다.
Unable to find image 'hello-world:latest' locally
latest: Pulling from library/hello-world
b8dfde127a29: Pull complete 
Digest: sha256:0fe98d7debd9049c50b597ef1f85b7c1e8cc81f59c8d623fcb2250e8bec85b38
Status: Downloaded newer image for hello-world:latest

Hello from Docker!
This message shows that your installation appears to be working correctly.

To generate this message, Docker took the following steps:
 1. The Docker client contacted the Docker daemon.
 2. The Docker daemon pulled the "hello-world" image from the Docker Hub.
    (amd64)
 3. The Docker daemon created a new container from that image which runs the
    executable that produces the output you are currently reading.
 4. The Docker daemon streamed that output to the Docker client, which sent it
    to your terminal.

To try something more ambitious, you can run an Ubuntu container with:
 $ docker run -it ubuntu bash

Share images, automate workflows, and more with a free Docker ID:
 https://hub.docker.com/

For more examples and ideas, visit:
 https://docs.docker.com/get-started/
```

현재 모든 docker 작업이 root 유저에게만 권한이 있기 때문에 docker 작업을 하기 위해선 명령 앞에 sudo를 붙여야 합니다.

예를 들어 다음과 같이 하면 됩니다.  
``` bash
sudo usermod -a -G docker $USER
sudo service docker restart
```

로그 아웃을 한 후 다시 로그인하면 다음과 같은 결과를 얻을 수 있습니다.  
``` shell
CONTAINER ID   IMAGE     COMMAND   CREATED   STATUS    PORTS     NAMES
```

## Docker의 기본적인 명령
<hr/>  

* Docker pull
docker image repository로부터 Docker Image를 가져오는 커맨드입니다.  
``` bash
$ docker pull --help

# 이 커맨드는 repository에 있는 ubuntu18.04 이미지를 불러온다.
docker pull ubuntu:18.04
```

* Docker images
로컬에 존재하는 docker image 리스트를 출력하는 커맨드 입니다.  
``` bash
$ docker images
```

* Docker ps
현재 실행 중인 도커 컨테이너 리스트를 출력하는 커맨드 입니다.
``` bash
$ docker ps
```

* Docker Run
도커의 컨테이너를 실행시키는 커맨드 입니다.
``` bash
$ docker run --help

#다음은 demo1 컨테이너를 실행시키는 커맨드 입니다.
docker run -it --name demo1 ubuntu:18.04 /bin/bash
```
* Docker exec
Docker 컨테이너 내부에서 명령을 내리거나 내부로 접속하는 커맨드 입니다.
``` bash
$ docker exec --help

#demo2 컨테이너 만들고 접속하기
$ docker run -it -d --name demo2 ubuntu:18.04
$ docker ps #만들어졌는지 확인
$ docker exec -it demo2 /bin/bash
```

* Docker Logs
도커 컨테이너의 log를 확인하는 커맨드이다.
``` bash
$ docker logs --help

# test 라는 이름의 busybox 이미지를 백그라운드에서 도커 컨테이너로 실행하여, 1초에 한 번씩 현재 시간을 출력하는 커맨드
$ docker run --name demo3 -d busybox sh -c "while true; do $(echo date); sleep 1; done"

$ docker logs demo3 -f #계속 지켜보면서 출력하는 커맨드
```

* Docker Stop
실행 중인 도커 컨테이너를 중단시키는 커맨드입니다.  
``` bash
$ docker stop demo3
$ docker stop demo2
$ docker stop demo1
```

* Docker rm
도커 컨테이너를 삭제하는 커맨드입니다.
``` bash
$ docker stop demo3
$ docker stop demo2
$ docker stop demo1
```

* Docker rmi
도커 이미지를 삭제하는 커맨드입니다.
``` bash
$ docker images
# busybox, ubuntu 가 있는 것을 확인하실 수 있습니다.
$ docker rmi ubuntu
```

