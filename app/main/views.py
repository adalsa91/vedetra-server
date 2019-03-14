from flask import request, render_template
from flask_paginate import Pagination, get_page_parameter
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
    page = request.args.get(get_page_parameter(), type=int, default=1)
    detections = VehicleDetection.query.paginate(max_per_page=10).items
    pagination = Pagination(page=page, total=VehicleDetection.query.count(), css_framework='bootstrap3')
    return render_template('detecciones.html', detections=detections, pagination=pagination)


@main.route('/trayectos', methods=['GET', 'POST'])
def trayectos():
    return render_template('trayectos.html')
