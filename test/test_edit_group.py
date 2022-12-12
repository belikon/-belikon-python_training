# -*- coding: utf-8 -*-

from model.group import Group
from random import *

def test_edit_some_group(app, db, check_ui):
    old_groups = db.get_group_list()
    group = Group(group_name="New Group")
    index = randrange(len(old_groups))
    group.id = old_groups[index].id
    if len(db.get_group_list()) == 0:
        app.group.create(Group(group_name="test", group_header="test logo", group_footer="test group"))
    app.group.test_edit_group_by_id(group.id, group)
    new_groups = db.get_group_list()
    assert len(old_groups) == len(new_groups)
    old_groups[index] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    if check_ui:
        assert sorted(new_groups, key=group.id_or_max()) == sorted(app.group.get_group_list(), key=group.id_or_max())


