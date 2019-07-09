from flask import request, url_for
from . import api
from ..models import Detection, detections_schema, detection_schema
from .. import db


@api.route('/detections/')
def get_detections():
    detections = Detection.query.all()
    return detections_schema.jsonify(detections)


@api.route('/detection/<int:detection_id>')
def get_detection(detection_id):
    detection = Detection.query.get_or_404(detection_id)
    return detection_schema.jsonify(detection)


@api.route('/detections/', methods=['POST'])
def new_detection():
    detection = detection_schema.load(request.json).data
    db.session.add(detection)
    db.session.commit()

    return detection_schema.jsonify(detection), 201, \
           {'Location': url_for('api.get_detection', detection_id=detection.id)}
