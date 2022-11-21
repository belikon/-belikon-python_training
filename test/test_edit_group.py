# -*- coding: utf-8 -*-

from model.group import Group

def test_edit_first_group(app):
    old_groups = app.group.get_group_list()
    group = Group(group_name="New Group")
    group.id = old_groups[0].id
    if app.group.count() == 0:
        app.group.create(Group(group_name="test", group_header="test logo", group_footer="test group"))
    app.group.test_edit_first_group(group)
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)
    old_groups[0] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)

'''
def test_edit_first_group(app):
    if app.group.count() == 0:
        app.group.create(Group(group_name="test", group_header="test logo", group_footer="test group"))
    app.group.test_edit_first_group_name(Group(group_name="edited"))

def test_edit_first_group_header(app):
    if app.group.count() == 0:
        app.group.create(Group(group_name="test", group_header="test logo", group_footer="test group"))
    app.group.test_edit_first_group_name(Group(group_header="edited"))
'''