from model.contact import Contact

def test_edit_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(
            # add info FIO and nikname
            abon_first_name="Testob",
            abon_middle_name="Ivanov",
            abon_last_name="Testovich",
            abon_nikname="Petrucho"))
    contact = Contact(
    #add info FIO and nikname
                                   abon_first_name="Testob",
                                   abon_middle_name="Testovich",
                                   abon_last_name="Ivanov")
    old_contacts = app.contact.get_contacts_list()
    contact.id = old_contacts[0].id
    app.contact.edit_first_contact(contact)
    new_contacts = app.contact.get_contacts_list()

    assert len(old_contacts) == len(new_contacts)
    old_contacts[0] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)



