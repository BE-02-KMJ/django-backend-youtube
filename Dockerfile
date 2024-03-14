# docker image 구축
# alpine: Linux 경량화 ver.
# Python 3.11이 설치된 Alpine Linux 3.19
FROM python:3.11-alpine3.19

# LABEL 명령어: 이미지의 유지관리자(메타데이터)를 추가하는 것.
LABEL maintainer="mingming96"

# Python 관련 로그 확인 옵션 코드. (기본값 0 = False)
ENV PYTHONUNBUFFERED 1

# 로컬에서 작업한 파일들을 가상환경으로 복사하는 코드
COPY ./requirements.txt /tmp/requirements.txt
COPY ./requirements.dev.txt /tmp/requirements.dev.txt
COPY ./app /app
WORKDIR /app
EXPOSE 8000

ARG DEV=False

# Linux → venv
# && \ : enter
RUN python -m venv /py && \
    /py/bin/pip install --upgrade pip && \
    /py/bin/pip install -r /tmp/requirements.txt && \
    # 개발 모드일 시 dev에서 실행
    if [ $DEV = "true"]; \  
        then /py/bin/pip install -r /tmp/requirements.dev.txt ; \
    fi && \
    # image 크기를 줄이기 위해 임의로 만든 폴더 삭제.
    rm -rf /tmp && \
    # 새로운 user 만들기
    adduser \
        --disabled-password \
        --no-create-home \
        django-user

ENV PATH="/scripts:/py/bin:$PATH"

USER django-user