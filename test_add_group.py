# _*_ config: utf-8 _*_
import pytest
from group import Group
from applycation import Applycation

@pytest.fixture
def app(request):
    fixture = Applycation()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_add_group(app):
    app.login(username="admin", password="secret")
    app.create_group(Group(name="qfgdfg", header="dfgdfg", footer="dfgfghgfhg"))
    app.logout()

def test_empty_group(app):
    app.login(username="admin", password="secret")
    app.create_group(Group(name="", header="", footer=""))
    app.logout()