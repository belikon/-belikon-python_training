# -*- coding: utf-8 -*-

from model.group import Group

def test_edit_first_group(app):
    app.session.Login(username="admin", password="secret")
    app.group.test_edit_first_group(Group(group_name="edited", group_header="test edit", group_footer="edit group"))
    app.session.Logout()
