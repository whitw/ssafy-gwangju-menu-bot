FROM python:3.11-alpine

RUN apk update && \
    ln -fs /usr/share/zoneinfo/Asia/Seoul /etc/localtime && \
    echo "Asia/Seoul" > /etc/timezone

RUN pip3 install beautifulsoup4 requests

WORKDIR /app

COPY gwangju-menubot.py gwangju-menubot.py

CMD ["/bin/sh"]
