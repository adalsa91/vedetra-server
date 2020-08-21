from flask import request, url_for
from . import api
from ..models import Detection, detections_schema, detection_schema
from .. import db


@api.route('/detections/')
def get_detections():
    detections = Detection.query.all()
    return detections_schema.jsonify(detections)


@api.route('/detections/<int:detection_id>')
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


@api.route('/detections-collection/', methods=['POST'])
def new_detections():
    detections_json = []
    for device, timestamp in request.json['detections'].items():
        detections_json.append({
            'md5_mac': device,
            'timestamp': timestamp,
            'sensor_id': request.json['node']
        })
    detections = detections_schema.load(detections_json).data
    db.session.add_all(detections)
    db.session.commit()

    return detections_schema.jsonify(detections_json), 201


@api.route('/detections/<detection_id>', methods=['DELETE'])
def delete_detection(detection_id):
    detection = Detection.query.get_or_404(detection_id)
    db.session.delete(detection)
    db.session.commit()

    return detection_schema.jsonify(detection), 200


@api.route('/detections/<detection_id>', methods=['PUT'])
def modify_detection(detection_id):
    detection = Detection.query.get_or_404(detection_id)
    detection_schema.load(request.json, instance=detection, partial=True)
    db.session.commit()

    return detection_schema.jsonify(detection), 200, \
           {'Location': url_for('api.get_detection', detection_id=detection.id)}
