
import pytest
from fixture.applycation import Applycation

@pytest.fixture (scope = "session")
def app(request):
    fixture = Applycation()
    request.addfinalizer(fixture.destroy)
    return fixture
