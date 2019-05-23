# _*_ config: utf-8 _*_
from model.group import Group

def test_add_group(app):
    app.session.login(username="admin", password="secret")
    app.group.create(Group(name="qfgdfg", header="dfgdfg", footer="dfgfghgfhg"))
    app.session.logout()

def test_empty_group(app):
    app.session.login(username="admin", password="secret")
    app.group.create(Group(name="", header="", footer=""))
    app.session.logout()