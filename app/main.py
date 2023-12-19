# app/main.py

from fastapi import FastAPI

from app.db import database, User

# создание экземпляра fastapi  с именем app и указанным заголоовком
app = FastAPI(title="FastAPI, Docker, and Traefik")


@app.get("/")
# используеться асинхронный метод????? как это происходитТ???? и в чем заключаеться????
async def read_root():
    return await User.objects.all()

# проверка события запуск
@app.on_event("startup")
async def startup():
    # если нет подключения к базе
    if not database.is_connected:
        # ожидать подключения к базе
        await database.connect()
    # выставить пользователю указанный емэйл. каждому???? если одному то которому?????
    await User.objects.all()
    #await User.objects.get_or_create(email="test@test.com")

# проверка на закрытие базы
@app.on_event("shutdown")
async def shutdown():
    if database.is_connected:
        await database.disconnect()
