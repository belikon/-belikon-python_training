from model.contact import Contact
from model.group import Group
from fixture.orm import ORMFixture
import random


def test_add_contacts_to_groups(app, orm, db):
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
    old_groups = orm.get_group_list()
    group = random.choice(old_groups)
    contact_not_in_group = orm.get_contacts_not_in_group(group)
    if len(contact_not_in_group) == 0:
        app.contact.create(contact)
    contact = random.choice(contact_not_in_group)
    app.contact.add_contact_in_group(contact.id, group.id)
    new_group_list = orm.get_contacts_in_group(group)
    assert contact in new_group_list

