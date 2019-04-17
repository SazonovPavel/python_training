# _*_ config: utf-8 _*_
import pytest
from model.group import Group
from fixture.applycation import Applycation

@pytest.fixture
def app(request):
    fixture = Applycation()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_add_group(app):
    app.session.login(username="admin", password="secret")
    app.create_group(Group(name="qfgdfg", header="dfgdfg", footer="dfgfghgfhg"))
    app.session.logout()

def test_empty_group(app):
    app.session.login(username="admin", password="secret")
    app.create_group(Group(name="", header="", footer=""))
    app.session.logout()