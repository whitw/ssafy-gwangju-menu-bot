FROM python:3.11-alpine

RUN apk update && \
    ln -fs /usr/share/zoneinfo/Asia/Seoul /etc/localtime && \
    echo "Asia/Seoul" > /etc/timezone

RUN pip3 install beautifulsoup4 requests

WORKDIR /app

COPY gwangju-menubot.py gwangju-menubot.py
COPY url_hook.txt url_hook.txt

RUN touch /app/bot.log
RUN echo "20 10 * * 1-5 /usr/local/bin/python3 /app/gwangju-menubot.py >> /app/bot.log" >> /etc/crontabs/root

CMD ["crond", "-f"]
