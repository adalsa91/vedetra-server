from . import api
from ..models import Detection, detections_schema, detection_schema


@api.route('/detections/')
def get_detections():
    detections = Detection.query.all()
    return detections_schema.jsonify(detections)


@api.route('/detection/<int:detection_id>')
def get_detection(detection_id):
    detection = Detection.query.get_or_404(detection_id)
    return detection_schema.jsonify(detection)
