# -*- coding: utf-8 -*-

from contact import Contact
from contact_application import Contact_Application
import pytest

@pytest.fixture
def app(request):
    fixture = Contact_Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_add_conctact(app):
    app.Login(username="admin", password="secret")
    app.create_abon_add_abon_info(Contact(
    #add info FIO and nikname
                                   abon_first_name="Petr",
                                   abon_middle_name="Ivanov",
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
                                    phone_fax="none",
    #add abonent add email and site
                                    email="test@mail.com",
                                    email2="test2@mail.com",
                                    email3="test3@mail.com",
                                    homepage="http://localhost"))

    app.logout()
