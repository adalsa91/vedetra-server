import os
from app import create_app, db
from app.models import Sensor, VehicleDetection
from tests.example_data import db_load_example_data

app = create_app(os.getenv('FLASK_CONFIG') or 'default')

@app.shell_context_processor
def make_shell_context():
    return dict(db=db, Sensor=Sensor, VehicleDetection=VehicleDetection)


@app.cli.command()
def test():
    """Run the unit tests."""
    db_load_example_data(app, db)
    import pytest
    pytest.main(['tests'])