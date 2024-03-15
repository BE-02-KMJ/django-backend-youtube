# Youtube REST API project

## 1일차
### - Project Setting
#### 1. Github
- repository 생성
- 로컬에 있는 내 컴퓨터 폴더와 github Remote 공간 연결
- git clone https://github.com/BE-02-KMJ/django-backend-youtube.git
- github 어렵다 싶으면 github desktop 프로그램 받기

#### 2. Docker Hub
- 내 컴퓨터에 가상환경을 구축하는 것
- https://www.docker.com/products/docker-desktop/ 페이지에서 컴퓨터에 맞는 Docker 프로그램을 설치한다.
- 회원가입이 되어 있지 않다면 회원가입까지 해주기
- Docker Account Settings 에서 Access Token 새로 발급 받기 (받은 토큰 보관 잘하기~!)
- Github에 Secret Action 등록하기. (User, Token)
- local에서 github으로 push하면 local에서 docker hub으로 가고 그 다음에 github에서 test까지 해주는 거라고 생각하면 된다.

#### 3. Django project setting
- requirements.txt(실제 배포 환경),  requirements.dev.txt(개발, 연습용) 파일 생성
- 둘 다 패키지 관리는 동일한데 실제 배포 환경과 개발 및 연습용 공간인 것이 다르다고 생각하면 된다.
- 실전: 패키지 의존성 관리 → 버전관리, 패키지들간의 관계 관리.

- Dockerfile 파일 생성
- .dockerignore 파일 생성
- .gitignore 파일 생성
(https://djangowaves.com/tips-tricks/gitignore-for-a-django-project/) 참고

- docker-compose.yml 파일 생성
- django 설치
- .flake8 파일 생성

- github action create(.github/workflows/checks.yml)
- git add / commit / push

## 2일차
### - PostgreSQL
#### 1. docker postgresql image pull
- docker-compose.yml 파일 수정
- Dockerfile 파일 수정
- requirements.txt 파일 수정
- app/settings.py 파일 수정

- 사용자 정의 django 명령어 만들기 
  - core 폴더 생성.

여기서 부터 발생한 미친 오류 발생...
"django.db.utils.OperationalError: connection to server on socket "/var/run/postgresql/.s.PGSQL.5432" failed: No such file or directory"
→ 파일 다 삭제하고 docker desktop에서도 Containers, Images, Builds 다 삭제한 후 다시 처음부터 다시 시작하니 잘 됐다.
역시 해결하지 못할 땐 다 삭제하고 처음부터! ㅎㅎㅎ