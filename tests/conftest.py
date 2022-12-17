import pytest

from main import create_app, db


@pytest.fixture
def app():
    app = create_app()
    app.config.update({
        'TESTING': True,
        'SQLALCHEMY_DATABASE_URI': 'f"postgresql://:memory:"'
    })

    with app.app_context():
        db.create_all()

    yield app

    # clean up/ reset ressources


@pytest.fixture
def client(app):
    return app.test_client()
