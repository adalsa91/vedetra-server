import os
from app import create_app, db
from app.models import Sensor, Detection

app = create_app(os.getenv('FLASK_CONFIG') or 'default')


@app.shell_context_processor
def make_shell_context():
    return dict(db=db, Sensor=Sensor, Detection=Detection)


@app.cli.command()
def test():
    """Run the unit tests."""
    import pytest
    pytest.main(['tests'])