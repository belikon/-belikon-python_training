from model.contact import Contact
from random import randrange

def test_delete_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(
            # add info FIO and nikname
            abon_first_name="Testob",
            abon_middle_name="Ivanov",
            abon_last_name="Testovich",
            abon_nikname="Petrucho"))
    old_contacts = app.contact.get_contacts_list()
    app.contact.delete_first_contact()
    new_contacts = app.contact.get_contacts_list()
    assert len(old_contacts) -1 == len(new_contacts)
    old_contacts[0:1] = []
    assert old_contacts == new_contacts

def test_delete_some_contact(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(
            # add info FIO and nikname
            abon_first_name="Testob",
            abon_middle_name="Ivanov",
            abon_last_name="Testovich",
            abon_nikname="Petrucho"))
    old_contacts = db.get_contact_list()
    index = randrange(len(old_contacts))
    app.contact.delete_contact_by_index(index)
    new_contacts = db.get_contact_list()
    assert len(old_contacts) -1 == len(new_contacts)
    if check_ui:
        assert sorted(old_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contacts_list(), key=Contact.id_or_max)