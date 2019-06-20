from flask import request, render_template
from flask_paginate import Pagination, get_page_parameter
from . import main

from ..models import Sensor, Detection


@main.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')


@main.route('/detections', methods=['GET', 'POST'])
def detections():
    page = request.args.get(get_page_parameter(), type=int, default=1)
    detections = Detection.query.paginate(max_per_page=10).items
    pagination = Pagination(page=page, total=Detection.query.count(), css_framework='bootstrap3')
    return render_template('detections.html', detections=detections, pagination=pagination)


@main.route('/trayectos', methods=['GET', 'POST'])
def trayectos():
    return render_template('trayectos.html')
