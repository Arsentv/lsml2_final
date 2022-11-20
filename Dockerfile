FROM python:3-slim

ENV PYTHONFAULTHANDLER=1
ENV PYTHONUNBUFFERED=1
ENV PYTHONHASHSEED=random
ENV PYTHONDONTWRITEBYTECODE 1
ENV PIP_NO_CACHE_DIR=off
ENV PIP_DISABLE_PIP_VERSION_CHECK=on
ENV PIP_DEFAULT_TIMEOUT=100

# Env vars
ENV TELEGRAM_TOKEN ${TELEGRAM_TOKEN}

RUN apt-get update
RUN apt-get install -y python3 python3-pip python-dev build-essential python3-venv

RUN mkdir -p /codebase /storage
ADD . /codebase
WORKDIR /codebase

RUN pip install -r requirements.txt
RUN pip install python-telegram-bot

RUN chmod +x /codebase/server.py

CMD python3 /codebase/telegram_bot.py;
