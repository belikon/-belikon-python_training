# -*- coding: utf-8 -*-

from model.group import Group
from fixture.application import Application
import pytest

@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_add_group(app):
    app.session.Login(username="admin", password="secret")
    app.group.create(Group(group_name="test", group_header="test logo", group_footer="test group"))
    app.session.logout()

def test_add_empty_group(app):
    app.session.Login(username="admin", password="secret")
    app.group.create(Group(group_name="", group_header="", group_footer=""))
    app.session.logout()

