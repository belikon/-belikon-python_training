from model.contact import Contact
import time

class ContactHelper:

    def __init__(self, app):
        self.app = app

    def open_page(self):
        wd = self.app.wd
        #if not (wd.current_url.endswith("/addressbook/") and len(wd.find_elements_by_name("entry")) > 0):
        if not wd.current_url == "http://localhost/addressbook/":
            wd.find_element_by_link_text("home").click()


    def create(self, contact):
        # test_add_contact.py
        wd = self.app.wd
        #open add new contact page
        self.open_page()
        wd.find_element_by_link_text("add new").click()
        #add new contact
        self.fill_contact_form(contact)
        wd.find_element_by_name("submit").click()


    def delete_first_contact(self):
        wd = self.app.wd
        self.open_page()
        wd.find_element_by_link_text("home").click()
        wd.find_element_by_name("selected[]").click()
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to.alert.accept()
        wd.find_element_by_css_selector("div.msgbox")
        #time.sleep(3)
        #self.open_page()


    def edit_first_contact(self, contact):
        wd = self.app.wd
        self.open_page()
        wd.find_element_by_xpath("//img[@alt='Edit']").click()
        # edit
        self.fill_contact_form(contact)
        # Update
        wd.find_element_by_name("update").click()
        self.open_page()
        time.sleep(2)

    def fill_contact_form(self, contact):
        wd = self.app.wd
        self.change_field_value("firstname", contact.abon_first_name)
        self.change_field_value("middlename", contact.abon_middle_name)
        self.change_field_value("lastname", contact.abon_last_name)
        self.change_field_value("nickname", contact.abon_nikname)
        self.change_field_value("company", contact.company)
        self.change_field_value("address", contact.address)
        self.change_field_value("title", contact.title)
        self.change_field_value("home", contact.phone_home)
        self.change_field_value("mobile", contact.phone_mobile)
        self.change_field_value("work", contact.phone_work)
        self.change_field_value("fax", contact.phone_fax)
        self.change_field_value("email", contact.email)
        self.change_field_value("email2", contact.email2)
        self.change_field_value("email3", contact.email3)
        self.change_field_value("homepage", contact.homepage)

    def change_field_value(self, field_name, test):
        wd = self.app.wd
        if test is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(test)

    def count(self):
        wd = self.app.wd
        self.open_page()
        return len(wd.find_elements_by_name("selected[]"))

    def get_contacts_list(self):
        wd = self.app.wd
        self.open_page()
        contacts_list = []
        for element in wd.find_elements_by_css_selector("tr.odd"):
            id = element.find_element_by_name("selected[]").get_attribute("value")
            fio_list = list(element.find_elements_by_tag_name("td"))
            abon_first_name = fio_list[2].text
            abon_middle_name = fio_list[1].text
            contacts_list.append(Contact(id = id, abon_first_name = abon_first_name, abon_middle_name = abon_middle_name))
        #print(contacts)
        return contacts_list
