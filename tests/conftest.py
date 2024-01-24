import pytest
from app import app as _app

@pytest.fixture()
def app():
    _app.config.update({
        "TESTING": True,
    })

    yield _app


@pytest.fixture()
def client(app):
    return _app.test_client()


@pytest.fixture()
def runner(app):
    return _app.test_cli_runner()
