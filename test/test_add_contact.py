# -*- coding: utf-8 -*-
from model.contact import Contact
import pytest
import random
import string

def test_new_add_conctact(app, db, json_contacts, check_ui):
    #pass
    old_contacts = db.get_contact_list()
    app.contact.create(json_contacts)
    new_contacts = db.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)
    old_contacts.append(json_contacts)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    if check_ui:
        assert sorted(old_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contacts_list(), key=Contact.id_or_max)


'''
def test_new_add_conctact(app, contact):

    contact = Contact(
    #add info FIO and nikname
                                   abon_first_name="Testob2",
                                   abon_middle_name="Testovich",
                                   abon_last_name="Testovich",
                                   abon_nikname="Petrucho",
    #add abonent info company, address and tittle
                                    company = "Gazprom",
                                    address = "Lubyznka32, 112",
                                    title = "test tittle",
    #add abonent phone info
                                    phone_home="749522212244",
                                    phone_mobile="79327665211",
                                    phone_work="88002000600",
                                    secondaryphone="234523",
    #add abonent add email and site
                                    email="test@mail.com",
                                    email2="test2@mail.com",
                                    email3="test3@mail.com",
                                    homepage="http://localhost")
    old_contacts = app.contact.get_contacts_list()
    app.contact.create(contact)
    new_contacts = app.contact.get_contacts_list()
    assert len(old_contacts) + 1 == len(new_contacts)
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
'''

