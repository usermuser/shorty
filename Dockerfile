#   использовать версию 3.10
FROM python:3.10
#   устанавливает рабочую директорию
WORKDIR /app
#   устанавливает постоянные переменные среды
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
#   копирвование requirements
COPY requirements.txt .
# запуск установки пакетов из requirements
RUN pip install -r requirements.txt
#  копировать приложение из каталога в обра
COPY . .
