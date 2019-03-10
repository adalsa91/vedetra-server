from flask import Flask, request, render_template
from . import main

from ..models import Sensor, VehicleDetection


@main.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')


@main.route('/base', methods=['GET', 'POST'])
def base():
    return render_template('base.html')


@main.route('/detecciones', methods=['GET', 'POST'])
def detecciones():
    detetections = VehicleDetection.query.limit(10).all()

    return render_template('detecciones.html', detections=detetections)


@main.route('/trayectos', methods=['GET', 'POST'])
def trayectos():
    return render_template('trayectos.html')
