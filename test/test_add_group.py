# -*- coding: utf-8 -*-

from model.group import Group
#import pytest
#import random
#import string
#from data.groups import constant as testdata


def test_add_group(app, db, json_groups, check_ui):
    group = json_groups
    #pass
    old_groups = db.get_group_list()
    app.group.create(group)
    new_groups = db.get_group_list()
    old_groups.append(group)
    if check_ui:
        assert sorted(new_groups, key=group.id_or_max()) == sorted(app.group.get_group_list(), key=group.id_or_max())
