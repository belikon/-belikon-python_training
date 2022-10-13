from model.contact import Contact

def test_edit_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(
            # add info FIO and nikname
            abon_first_name="Testob",
            abon_middle_name="Ivanov",
            abon_last_name="Testovich",
            abon_nikname="Petrucho"))
    app.contact.edit_first_contact(Contact(
    #add info FIO and nikname
                                   abon_first_name="Edit",
                                   abon_middle_name="IvanovEditor",
                                   abon_last_name="Testovich",
                                   abon_nikname="PetruchoED",
    #add abonent info company, address and tittle
                                    company = "GazpromOPN",
                                    address = "Lubyznka",
                                    title = " ",
                                    phone_home=" wer",
                                    phone_mobile="234 ",
                                    phone_work="234 ",
                                    phone_fax="243 ",
    #add abonent add email and site
                                    email="test@mail.ru",
                                    email2="test2@m23ail.com",
                                    email3="test3@ .com",
                                    homepage="http:// "))

def test_new_edit_first_contact(app):
    app.contact.edit_first_contact(Contact(abon_first_name="Editort"))
