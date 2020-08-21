from flask import request, url_for
from . import api
from ..models import Sensor, sensor_schema, sensors_schema
from .. import db


@api.route('/sensors/')
def get_sensors():
    sensors = Sensor.query.all()
    return sensors_schema.jsonify(sensors)


@api.route('/sensors/<sensor_id>')
def get_sensor(sensor_id):
    sensor = Sensor.query.get_or_404(sensor_id)
    return sensor_schema.jsonify(sensor)


@api.route('/sensors/', methods=['POST'])
def new_sensor():
    sensor = sensor_schema.load(request.json, session=db.session).data
    db.session.add(sensor)
    db.session.commit()

    return sensor_schema.jsonify(sensor), 201, \
           {'Location': url_for('api.get_sensor', sensor_id=sensor.id)}


@api.route('/sensors/<sensor_id>', methods=['DELETE'])
def delete_sensor(sensor_id):
    sensor = Sensor.query.get_or_404(sensor_id)
    db.session.delete(sensor)
    db.session.commit()

    return sensor_schema.jsonify(sensor), 200


@api.route('/sensors/<sensor_id>', methods=['PUT'])
def modify_sensor(sensor_id):
    sensor = Sensor.query.get_or_404(sensor_id)
    sensor_schema.load(request.json, instance=sensor, partial=True)
    db.session.commit()

    return sensor_schema.jsonify(sensor), 200, \
           {'Location': url_for('api.get_sensor', sensor_id=sensor.id)}
