#   использовать версию 3.10
FROM python:3.10
#   устанавливает рабочую директорию
WORKDIR /code
#   уточнить похоже на установку виртуального окружения
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
#   копирвование requirements
COPY ./requirements.txt /code/requirements.txt
# запуск установки пакетов из requirements
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
#  копировать  app  в  code/app
COPY ./app /code/app
