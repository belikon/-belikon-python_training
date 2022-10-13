# -*- coding: utf-8 -*-

from model.group import Group

def test_add_group(app):
    app.group.create(Group(group_name="test", group_header="test logo", group_footer="test group"))
    app.session.Logout()

def test_add_empty_group(app):
    app.group.create(Group(group_name="1", group_header="2", group_footer="3"))

