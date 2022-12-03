# -*- coding: utf-8 -*-
from model.contact import Contact
import pytest
import random
import string

def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])
"""
testdata = [
    Contact(abon_first_name=abon_first_name, abon_middle_name=abon_middle_name, abon_last_name=abon_last_name, address = address,
            phone_home = phone_home, phone_mobile = phone_mobile, phone_work = phone_work, secondaryphone = secondaryphone,
            email = email, email2 = email2, email3 = email3 )
    for abon_first_name in ["", random_string("abon_first_name", 10)]
    for abon_middle_name in ["", random_string("abon_middle_name", 20)]
    for abon_last_name in ["", random_string("abon_last_name", 20)]
    for address in ["", random_string("address", 20)]
    for phone_home in ["", random_string("phone_home", 20)]
    for phone_mobile in ["", random_string("phone_mobile", 20)]
    for phone_work in ["", random_string("phone_work", 20)]
    for secondaryphone in ["", random_string("secondaryphone", 20)]
    for email in ["", random_string("email", 20)]
    for email2 in ["", random_string("email2", 20)]
    for email3 in ["", random_string("email3", 20)]
]
"""
testdata = [Contact(abon_first_name="", abon_middle_name="", abon_last_name="", address = "",
            phone_home = "", phone_mobile = "", phone_work = "", secondaryphone = "",
            email = "", email2 = "", email3 = "" )] + [
    Contact(abon_first_name=random_string("abon_first_name", 10),
            abon_middle_name=random_string("abon_middle_name", 20),
            abon_last_name=random_string("abon_last_name", 20),
            address=random_string("address", 20),
            phone_home=random_string("phone_home", 20),
            phone_mobile=random_string("phone_mobile", 20),
            phone_work=random_string("phone_work", 20),
            secondaryphone=random_string("secondaryphone", 20),
            email=random_string("email", 20), email2=random_string("email2", 20), email3=random_string("email3", 20))
    for i in range(5)
]


@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])

def test_new_add_conctact(app, contact):
    #pass
    old_contacts = app.contact.get_contacts_list()
    app.contact.create(contact)
    new_contacts = app.contact.get_contacts_list()
    assert len(old_contacts) + 1 == len(new_contacts)
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


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

