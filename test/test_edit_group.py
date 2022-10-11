# -*- coding: utf-8 -*-

from model.group import Group

def test_edit_first_group(app):
    if app.group.count() == 0:
        app.group.create(Group(group_name="test", group_header="test logo", group_footer="test group"))
    app.group.test_edit_first_group(Group(group_name="edited", group_header="test edit", group_footer="edit group"))

def test_edit_first_group(app):
    if app.group.count() == 0:
        app.group.create(Group(group_name="test", group_header="test logo", group_footer="test group"))
    app.group.test_edit_first_group_name(Group(group_name="edited"))

def test_edit_first_group_header(app):
    if app.group.count() == 0:
        app.group.create(Group(group_name="test", group_header="test logo", group_footer="test group"))
    app.group.test_edit_first_group_name(Group(group_header="edited"))
