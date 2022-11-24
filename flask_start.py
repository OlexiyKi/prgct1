from flask import Flask, request
from random import randint
from utils import get_currency_exchange_rate, get_pb_exchange_rate, create_password

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p><b>Hello, World!</b></p>"


@app.route("/rates", methods=['GET'])
def get_rates():
    currency_a = request.args.get('currency_a', default='USD')
    currency_b = request.args.get('currency_b', default='UAH')
    result = get_currency_exchange_rate(currency_a, currency_b)
    return result


@app.route("/rates_pb", methods=['GET'])
def get_pb_rates():
    convert_currency = request.args.get('convert_currency', default='USD')     #вытаскиваем параметры с URL
    bank = request.args.get('bank', default='NBU') # TODO додати функцію валідації вводу банку
    rate_date = request.args.get('rate_date', default='01.11.2022')
    # как request.args.get получает урл если еще не выполнился   resul
    result = get_pb_exchange_rate(convert_currency, bank, rate_date)           #запускаем основную ф-ю с параметрами с URL
    return result


@app.route("/password", methods=['GET'])
def get_password():
    """
    3) Створити вью-функцію, яка як параметри отримує імʼя та вік, а повертає фразу:
    "Привіт, імʼя! Твій пароль: пароль".
    Генерувати рандомний пароль, який містить стільки ж знаків, скільки вік користувача.
    """
    name = request.args.get('name', default='No name')
    age = request.args.get('age', default=0)

    result = create_password(name, age)

    return result