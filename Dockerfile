FROM python:3.11-alpine

RUN apk update && \
    ln -fs /usr/share/zoneinfo/Asia/Seoul /etc/localtime && \
    echo "Asia/Seoul" > /etc/timezone

RUN pip3 install beautifulsoup4 requests

WORKDIR /app

COPY gwangju-menubot.py gwangju-menubot.py
COPY url_hook.txt url_hook.txt

RUN touch /app/bot.log
RUN touch /app/cron.log
RUN echo "* * * * * echo Hello! >> /app/bot.log 2>&1" | crontab -

ENTRYPOINT ["crond", "-l", "8", "-L", "/app/cron.log"]
CMD ["/bin/sh"]
