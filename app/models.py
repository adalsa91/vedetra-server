from . import db


class Sensor(db.Model):
    id = db.Column(db.String(32), primary_key=True, index=True)
    description = db.Column(db.String(200))
    detections = db.relationship('VehicleDetection', backref='sensor', lazy=True)

    def __repr__(self):
        return 'Sensor {}, {}'.format(self.id, self.description)


class VehicleDetection(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    md5_mac = db.Column(db.String(32), index=True)
    timestamp = db.Column(db.DateTime, nullable=False)
    sensor_id = db.Column(db.String(32), db.ForeignKey('sensor.id'), nullable=False)

    def __repr__(self):
        return 'Detection {}, MD5_MAC: {}, timestamps: {}, sensor: {}'.format(self.id, self.md5_mac, self.timestamp, self.sensor_id)
