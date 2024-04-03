#  Python 3.11이 설치된 Alpine Linux 3.19
# Alpine Linux는 경량화된 리눅스 배포판으로, 컨테이너 환경에 적합
FROM python:3.12

# LABEL 명령어는 이미지에 메타데이터를 추가합니다. 여기서는 이미지의 유지 관리자를 "seopftware"로 지정하고 있습니다.
LABEL maintainer="Minjung"

# 환경 변수 PYTHONUNBUFFERED를 1로 설정합니다. 
# 이는 Python이 표준 입출력 버퍼링을 비활성화하게 하여, 로그가 즉시 콘솔에 출력되게 합니다. 
# 이는 Docker 컨테이너에서 로그를 더 쉽게 볼 수 있게 합니다.
ENV PYTHONUNBUFFERED 1

# 로컬 파일 시스템의 requirements.txt 파일을 컨테이너의 /tmp/requirements.txt로 복사합니다. 
# 이 파일은 필요한 Python 패키지들을 명시합니다.
COPY ./requirements.txt /tmp/requirements.txt
COPY ./requirements.dev.txt /tmp/requirements.dev.txt
COPY ./app /app
COPY ./scripts /scripts

# Docker 컨테이너 내에서 작업 디렉토리를 /app으로 설정합니다. 
# 이후의 명령어들은 이 디렉토리를 기준으로 실행됩니다.
WORKDIR /app
# 컨테이너의 8000 포트를 외부에 노출시킵니다. 이는 애플리케이션이 해당 포트를 사용하여 통신한다는 것을 의미합니다.
EXPOSE 8000

# ARG 명령어는 빌드 시간에 사용할 변수를 정의합니다. 여기서는 DEV 변수를 false로 초기화합니다. 
# 이 변수는 개발 환경인지 아닌지를 나타내며, 뒤에 나오는 조건문에서 사용됩니다.

ARG DEV=false
RUN apk add --update --no-cache libffi-dev
RUN python -m venv /py && \
    /py/bin/pip install --upgrade pip && \
    /py/bin/pip install -r /tmp/requirements.txt && \
    apt-get update && \
    apt-get install -y postgresql-client build-essential libpq-dev zlib1g zlib1g-dev && \
    if [ "$DEV" = "true" ] ; \
        then echo "===THIS IS DEVELOPMENT BUILD===" && \
        /py/bin/pip install -r /tmp/requirements.dev.txt ; \
    fi && \
    apt-get remove -y --purge build-essential libpq-dev && \
    apt-get clean && \
    rm -rf /tmp && \
    adduser \
        --disabled-password \
        --no-create-home \
        django-user && \
    mkdir -p /vol/web/media && \
    mkdir -p /vol/web/static && \
    # chmod : change mode, chown : change owner
    chown -R django-user:django-user /vol && \
    # 폴더에 대한 접근 권한부여 
    chmod -R 755 /vol && \
    # 권한 적용
    chmod -R +x /scripts

ENV PATH="/scripts:/py/bin:$PATH"
USER django-user
CMD ["run.sh"]