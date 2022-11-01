from model.group import Group

def test_delete_first_group(app):
    if app.group.count() == 0:
        app.group.create(Group(group_name="test", group_header="test logo", group_footer="test group"))
    app.group.delete_first_group()
    #app.session.Logout()

def test_new_delete_first_group(app):
    if app.group.count() == 0:
        app.group.create(Group(group_name="test", group_header="test logo", group_footer="test group"))
    app.group.delete_first_group()

def test_new1_delete_first_group(app):
    if app.group.count() == 0:
        app.group.create(Group(group_name="test", group_header="test logo", group_footer="test group"))
    app.group.delete_first_group()

def test_new2_delete_first_group(app):
    if app.group.count() == 0:
        app.group.create(Group(group_name="test", group_header="test logo", group_footer="test group"))
    app.group.delete_first_group()