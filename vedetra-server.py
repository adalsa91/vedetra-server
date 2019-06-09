import os
from app import create_app, db
from app.models import Sensor, Detection

app = create_app(os.getenv('FLASK_CONFIG') or 'default')

@app.before_first_request
def load_dummy_data():
    with app.app_context():
        if os.getenv("LOAD_DUMMY_DATA", "false").lower() == "true":
            from tests.example_data import db_load_example_data

            db_load_example_data(app, db)

@app.shell_context_processor
def make_shell_context():
    return dict(db=db, Sensor=Sensor, Detection=Detection)


@app.cli.command()
def test():
    """Run the unit tests."""
    import pytest
    pytest.main(['tests'])