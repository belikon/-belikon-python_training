import  re
from random import randrange

def test_phones_on_home_page (app):
    contact_from_homepage = app.contact.get_contacts_list()[0]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_homepage.all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_edit_page)


def test_phones_on_contact_view_page(app):
    contact_from_view_page = app.contact.get_contact_from_view_page(0)
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_view_page.phone_home == contact_from_edit_page.phone_home
    assert contact_from_view_page.phone_work == contact_from_edit_page.phone_work
    assert contact_from_view_page.phone_mobile == contact_from_edit_page.phone_mobile
    assert contact_from_view_page.secondaryphone == contact_from_edit_page.secondaryphone

def clear(s):
    return re.sub("[()-]", "", s)

def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                     map(lambda x: clear(x),
                         filter(lambda x: x is not None,
                                [contact.phone_home, contact.phone_mobile, contact.phone_work, contact.secondaryphone]))))

def test_home_VS_edit_page_contact(app):
    index = randrange(len(app.contact.get_contacts_list()))

    contact_from_homepage = app.contact.get_contacts_list()[index]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
    assert contact_from_homepage.abon_first_name == contact_from_edit_page.abon_first_name
    assert contact_from_homepage.abon_last_name == contact_from_edit_page.abon_last_name
    assert contact_from_homepage.address == contact_from_edit_page.address
    assert contact_from_homepage.all_email_from_home_page == merge_email_like_on_home_page(contact_from_edit_page)
    assert contact_from_homepage.all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_edit_page)

def merge_email_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                     filter(lambda x: x is not None,[contact.email, contact.email2, contact.email3 ])))


#self.contact_cache.append(Contact(id = id, abon_first_name = abon_first_name, abon_last_name = abon_last_name, all_phones_from_home_page = all_phones,
#                                                  address = abon_address, all_email_from_home_page = abon_all_email))