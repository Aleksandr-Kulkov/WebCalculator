import os

from flask import Flask, render_template, render_template_string
from flask import request

from config import CONFIG, DIR_PREFIX


app = Flask(__name__, template_folder='static')


@app.route('/concate/<first>/<second>')
def concate(first, second):
    return render_template_string(f'<h1>{first + second}</h1>')


@app.route('/subtract/<first>/<second>')
def subtract(first, second):
    return render_template_string(f'<h1>{int(float(first) - float(second))}</h1>')


@app.route('/multiple/<first>/<second>')
def multiple(first, second):
    return render_template_string(f'<h1>{int(float(first) * float(second))}</h1>')


@app.route('/division/<first>/<second>')
def division(first, second):
    return render_template_string(f'<h1>{float(first) // float(second)}</h1>')


@app.route('/exponent/<first>/<second>')
def exponent(first, second):
    return render_template_string(f'<h1>{int(float(first) ** float(second))}</h1>')


@app.route('/')
def main():
    return render_template('index.html')


def run():
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.run(host='localhost', port=9023)
