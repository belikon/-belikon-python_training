from model.contact import Contact
def test_delete_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(
            # add info FIO and nikname
            abon_first_name="Testob",
            abon_middle_name="Ivanov",
            abon_last_name="Testovich",
            abon_nikname="Petrucho"))
    app.contact.delete_first_contact()
