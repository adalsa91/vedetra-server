from app.models import Sensor, VehicleDetection
from datetime import datetime
from binascii import b2a_hex
from os import urandom


def db_load_example_data(app, db):
    sensors = []
    for i in range(5):
        sensors.append(Sensor(id=b2a_hex(urandom(16)), description="Sensor {}".format(i)))

    vehicle_detections = []
    for i in range(20):
        vehicle_detections.append(VehicleDetection(md5_mac=b2a_hex(urandom(16)), timestamp=datetime.now(), sensor_id=sensors[i%5].id))

    with app.app_context():
        db.session.add_all(sensors)
        db.session.add_all(vehicle_detections)
        db.session.commit()
