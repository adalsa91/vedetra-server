from . import db
from . import ma


class Sensor(db.Model):
    id = db.Column(db.String(32), primary_key=True, index=True)
    description = db.Column(db.String(200))
    detections = db.relationship('Detection', backref='sensor', lazy=True)

    def __repr__(self):
        return 'Sensor {}, {}'.format(self.id, self.description)


class Detection(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    md5_mac = db.Column(db.String(32), index=True)
    timestamp = db.Column(db.DateTime, nullable=False)
    sensor_id = db.Column(db.String(32), db.ForeignKey('sensor.id'), nullable=False)

    def __repr__(self):
        return 'Detection {}, MD5_MAC: {}, timestamps: {}, sensor: {}'.format(self.id, self.md5_mac, self.timestamp,
                                                                              self.sensor_id)


class DetectionSchema(ma.ModelSchema):
    class Meta:
        model = Sensor
        # Fields to expose
        fields = ("md5_mac", "timestamp", "sensor_id")
        # Smart hyperlinking
        _links = ma.Hyperlinks(
            {"self": ma.URLFor("api.detections")}
        )


detection_schema = DetectionSchema()
detections_schema = DetectionSchema(many=True)
