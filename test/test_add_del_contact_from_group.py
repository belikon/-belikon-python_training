from model.contact import Contact
from model.group import Group
import random

def test_add_contact_in_group(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(
            # add info FIO and nikname
            abon_first_name="Testob",
            abon_middle_name="Ivanov",
            abon_last_name="Testovich",
            abon_nikname="Petrucho"))
    if len(db.get_group_list()) == 0:
        app.group.create(Group(group_name="test", group_header="test logo", group_footer="test group"))

    old_groups = db.get_group_list()
    old_contacts = db.get_contact_list()
    selection_group = random.choice(old_groups)
    selection_contact = random.choice(old_contacts)
    app.contact.add_contact_in_group(selection_contact.id, selection_group.id)
    assert len(old_contacts) == len(db.get_contact_list())
    if check_ui:
        assert sorted(old_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contacts_list(), key=Contact.id_or_max)

def test_delete_contact_from_group(app, db):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(
            # add info FIO and nikname
            abon_first_name="Testob",
            abon_middle_name="Ivanov",
            abon_last_name="Testovich",
            abon_nikname="Petrucho"))
    if len(db.get_group_list()) == 0:
        app.group.create(Group(group_name="test", group_header="test logo", group_footer="test group"))

    old_groups = db.get_group_list()
    #old_contacts = db.get_contact_list()
    selection_group = random.choice(old_groups)
    #selection_contact = random.choice(old_contacts)
    app.contact.delete_contact_from_group(selection_group.id)
