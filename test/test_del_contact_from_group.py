from model.contact import Contact
from model.group import Group

import random

def test_delete_contact_from_group(app, orm, db):
    contact = Contact(
        # add info FIO and nikname
        abon_first_name="Testob",
        abon_middle_name="Ivanov",
        abon_last_name="Testovich",
        abon_nikname="Petrucho")
    if len(db.get_contact_list()) == 0:
        app.contact.create(contact)
    if len(db.get_group_list()) == 0:
        app.group.create(Group(group_name="test", group_header="test logo", group_footer="test group"))
        group_list = orm.get_group_list()
        group = random.choice(group_list)
        if len(orm.get_contacts_in_group(Group(id=group.id))) == 0:
            contact = random.choice(orm.get_contact_list())
            app.contact.add_contact_in_group(contact.id, group.id)
        old_contacts_in_group = orm.get_contacts_in_group(Group(id=group.id))
        contact = random.choice(old_contacts_in_group)
        app.contact.delete_contact_from_group(contact.id)
        new_contacts_in_group = orm.get_contacts_in_group(Group(id=group.id))
        assert contact not in new_contacts_in_group
