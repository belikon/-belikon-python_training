# -*- coding: utf-8 -*-

from model.group import Group

def test_edit_first_group(app):
    app.group.test_edit_first_group(Group(group_name="edited", group_header="test edit", group_footer="edit group"))

def test_edit_first_group_name(app):
    app.group.test_edit_first_group_name(Group(group_name="edited"))

def test_edit_first_group_header(app):
    app.group.test_edit_first_group_name(Group(group_header="edited"))
