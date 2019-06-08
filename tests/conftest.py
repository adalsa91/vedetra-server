import pytest
from flask import Flask
from app import create_app, db
from tests.example_data import db_load_example_data


@pytest.fixture
def app():
    app = create_app('testing')  # type: Flask
    with app.app_context():
        db.create_all()
        db_load_example_data(app, db)

    yield app

    with app.app_context():
        db.session.remove()
        db.drop_all()


@pytest.fixture
def client(app):
    return app.test_client()


@pytest.fixture
def runner(app):
    return app.test_cli_runner()
