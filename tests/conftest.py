from app import app as test_app 
import pytest

@pytest.fixture()
def testing_app():
    test_app.config.update({
        "TESTING":True,
    })
    
    yield test_app

@pytest.fixture()
def client(testing_app):
    return testing_app.test_client()
    return test_app.test_client()
