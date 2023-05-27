import os
from flask import Flask, send_from_directory
from data import facts_list
from random import choice

app = Flask(__name__)


@app.route('/')
def home():
    return '<h1 style="color: red;">Привет!</h1><h1>Этот сайт поможет тебе узнать интересные факты о тех.зависимостях!</h1><a href="/random_fact" style="font-size: 20px;">Перейти</a>'


@app.route('/random_fact')
def random_fact():
    return f'<h2>{choice(facts_list)}</h2><h1>На нашем сайте есть страница со случайными мемами!</h1><a href="/random_meme" style="font-size: 20px;">Перейти</a>'


@app.route('/random_meme')
def random_meme():
    image = choice(os.listdir('images'))
    return send_from_directory('images', image) # пришлось спросить у ChatGPT как реализовать подобное)

app.run(debug=True)
