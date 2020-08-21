import os
import sys
import click
from flask_migrate import upgrade

COV = None
if os.environ.get('FLASK_COVERAGE'):
    import coverage

    COV = coverage.coverage(branch=True, source=['app'], include='app/*', data_file='./coverage/.coverage')
    COV.start()

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
@click.option('--coverage/--no-coverage', default=False,
              help='Run test under code coverage.')
def test(coverage):
    """Run the unit tests."""
    if coverage and not os.environ.get('FLASK_COVERAGE'):
        os.environ['FLASK_COVERAGE'] = '1'
        os.execvp(sys.executable, [sys.executable] + sys.argv)
    import pytest
    pytest.main(['tests'])
    if COV:
        COV.stop()
        COV.save()
        print("Coverage report:")
        COV.report()


@app.cli.command()
def deploy():
    """Run deployment tasks."""
    upgrade()
