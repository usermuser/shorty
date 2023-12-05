FROM python:3.10

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./test_fastapi.py /code/
COPY ./test.py /code/

CMD ['uvicorn', 'test_fastapi:app', '--host', '0.0.0.0', '--port', '80']