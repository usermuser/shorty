# shorty
links shortener

Сокращатель ссылок.

БД postgres in docker :
1. Длинная ссылка.
2. Короткая ссылка.

Эндпоинты:

- POST: запрос на создание ссылки:
  строка - длинная ссылка.
  В ответе короткая ссылка.
  
- GET: запрос по короткой ссылке,
  мы редиректим на длинную ссылку.

python version: 3.11-slim in docker

docker manuals:
https://tecadmin.net/how-to-dockerize-python-fastapi-application/


DB:

User:
user_id: positiveinteger
email: charfield(max_length=128)
created: datetime

URL:
url_id: positiveinteger
long_url: charfield(max_length=256) # unique
short_url: charfield(max_length=4)
created: datetime

Stat:
url_id: positiveinteger  -> ormar.ForeignKey(Url)
request_ip: ip_field
used_date: datetime

Switch:
user_id:
url_id:


Models:

class User(ormar.Model):
    class Meta:
        database = database
        metadata = metadata

    user_id: int = ormar.Integer(primary_key=True)
    email: str = ormar.String(max_length=128)
    created: ormar.DateTime(timezone=True)
