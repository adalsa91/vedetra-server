from _datetime import datetime
from flask import Flask, request, render_template
from . import main
from .. import db


@main.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')


@main.route('/base', methods=['GET', 'POST'])
def base():
    return render_template('base.html')


@main.route('/detecciones', methods=['GET', 'POST'])
def detecciones():
    return render_template('detecciones.html')


@main.route('/trayectos', methods=['GET', 'POST'])
def trayectos():
    return render_template('trayectos.html')
