from model.contact import Contact
from random import randrange

def test_edit_some_contact(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(
            # add info FIO and nikname
            abon_first_name="Testob",
            abon_middle_name="Ivanov",
            abon_last_name="Testovich",
            abon_nikname="Petrucho"))
    contact = Contact(
    #add info FIO and nikname
                                   abon_first_name="Testob",
                                   abon_middle_name="Testovich")
    old_contacts = db.get_contact_list()
    index = randrange(len(old_contacts))
    contact.id = old_contacts[index].id
    app.contact.edit_contact_by_index(index, contact)
    new_contacts = db.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[index] = contact
    if check_ui:
        assert sorted(old_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contacts_list(), key=Contact.id_or_max)

