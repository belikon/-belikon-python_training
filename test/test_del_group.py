import random

from model.group import Group
import random

def test_delete_some_id_group(app, db, check_ui):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(group_name="test", group_header="test logo", group_footer="test group"))
    old_groups = db.get_group_list()
    group = random.choice(old_groups)
    app.group.delete_group_by_id(group.id)
    new_groups = db.get_group_list()
    assert len(old_groups) - 1 == len(new_groups)
    old_groups.remove(group)
    assert old_groups == new_groups
    if check_ui:
        assert sorted(new_groups, key=group.id_or_max()) == sorted(app.group.get_group_list(), key=group.id_or_max())
'''
def test_delete_some_group(app):
    if app.group.count() == 0:
        app.group.create(Group(group_name="test", group_header="test logo", group_footer="test group"))
    old_groups = app.group.get_group_list()
    index = random.randrange(len(old_groups))
    app.group.delete_group_by_index(index)
    new_groups = app.group.get_group_list()
    assert len(old_groups) - 1 == len(new_groups)
    old_groups[index:index+1] = []
    assert old_groups == new_groups
'''