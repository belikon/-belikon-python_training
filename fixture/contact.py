from model.contact import Contact
import time
import re
import random

class ContactHelper:

    def __init__(self, app):
        self.app = app

    def open_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/addressbook/") and len(wd.find_elements_by_name("entry")) > 0):
        #if not wd.current_url == "http://localhost/addressbook/":
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
        self.contact_cache = None

    def select_contact_by_index(self, index):
        wd = self.app.wd
        self.open_page()
        wd.find_elements_by_name("selected[]")[index].click()

    def delete_contact_by_index(self, index):
        wd = self.app.wd
        self.open_page()
        self.select_contact_by_index(index)
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to.alert.accept()
        wd.find_element_by_css_selector("div.msgbox")
        #time.sleep(3)
        #self.open_page()
        self.contact_cache = None

    def delete_contact_by_id(self, id):
        wd = self.app.wd
        self.open_page()
        self.select_contact_by_id(id)
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to.alert.accept()
        wd.find_element_by_css_selector("div.msgbox")
        #time.sleep(3)
        #self.open_page()
        self.contact_cache = None

    def delete_first_contact(self):
        self.delete_contact_by_index(0)


    def edit_first_contact(self, contact):
        self.edit_contact_by_index(0, contact)

    def edit_contact_by_index(self, index, contact):
        wd = self.app.wd
        self.open_page()
        self.select_contact_by_index(index)
        wd.find_elements_by_xpath("//img[@alt='Edit']")[index].click()
        # edit
        self.fill_contact_form(contact)
        # Update
        wd.find_element_by_name("update").click()
        self.open_page()
        time.sleep(2)
        self.contact_cache = None

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
        #self.change_field_value("fax", contact.phone_fax)
        self.change_field_value("email", contact.email)
        self.change_field_value("email2", contact.email2)
        self.change_field_value("email3", contact.email3)
        self.change_field_value("homepage", contact.homepage)
        self.change_field_value("phone2", contact.secondaryphone)


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


    contact_cache = None

    def get_contacts_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.open_page()
            self.contact_cache = []
            #for element in wd.find_elements_by_css_selector("tr.odd"):
            for element in wd.find_elements_by_name("entry"):
                id = element.find_element_by_name("selected[]").get_attribute("value")
                cells = list(element.find_elements_by_tag_name("td"))
                #id = cells[0].find_element_by_tag_name("input").get_attribute("value")
                abon_first_name = cells[2].text
                abon_last_name = cells[1].text
                abon_address = cells[3].text
                abon_all_email = cells[4].text
                all_phones = cells[5].text
                self.contact_cache.append(Contact(id = id, abon_first_name = abon_first_name, abon_last_name = abon_last_name, all_phones_from_home_page = all_phones,
                                                  address = abon_address, all_email_from_home_page = abon_all_email))
            #print(contacts)
        return list(self.contact_cache)

    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.select_contact_by_index(index)
        wd.find_elements_by_xpath("//img[@alt='Edit']")[index].click()
        abon_first_name = wd.find_element_by_name("firstname").get_attribute("value")
        abon_last_name = wd.find_element_by_name("lastname").get_attribute("value")
        id = wd.find_element_by_name("id").get_attribute("value")
        phone_home = wd.find_element_by_name("home").get_attribute("value")
        phone_work = wd.find_element_by_name("work").get_attribute("value")
        phone_mobile = wd.find_element_by_name("mobile").get_attribute("value")
        secondaryphone = wd.find_element_by_name("phone2").get_attribute("value")
        abon_edit_address = wd.find_element_by_name("address").get_attribute("value")
        abon_edit_email = wd.find_element_by_name("email").get_attribute("value")
        abon_edit_email2 = wd.find_element_by_name("email2").get_attribute("value")
        abon_edit_email3 = wd.find_element_by_name("email3").get_attribute("value")
        secondary_edit_adress = wd.find_element_by_name("address2").get_attribute("value")
        return Contact(abon_first_name = abon_first_name, abon_last_name = abon_last_name, id = id,
                       phone_home = phone_home, phone_work = phone_work, phone_mobile = phone_mobile, secondaryphone = secondaryphone,
                       address = abon_edit_address, email = abon_edit_email, email2 = abon_edit_email2, email3 = abon_edit_email3, secondary_address = secondary_edit_adress)

    def open_contact_view_by_index(self, index):
        wd = self.app.wd
        self.open_page()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("tg")[6]
        cell.find_element_by_tag_name("a").click()

    def get_contact_from_view_page(self, index):
        wd = self.app.wd
        wd.find_elements_by_xpath("//img[@alt='Details']")[index].click()
        text = wd.find_element_by_id("content").text
        phone_home = re.search("H: (.*)", text).group(1)
        phone_work = re.search("W: (.*)", text).group(1)
        phone_mobile = re.search("M: (.*)", text).group(1)
        secondaryphone = re.search("P: (.*)", text).group(1)
        return Contact(phone_home = phone_home, phone_work = phone_work, phone_mobile = phone_mobile, secondaryphone = secondaryphone)
    def edit_contact_by_id(self, id, contact):
        wd = self.app.wd
        self.open_page()
        self.select_contact_by_id(id)
        wd.find_element_by_xpath('//a[@href="edit.php?id=%s"]' %int(id)).click()
        # edit
        self.fill_contact_form(contact)
        # Update
        wd.find_element_by_name("update").click()
        self.open_page()
        #time.sleep(2)
        self.contact_cache = None
    def add_contact_in_group(self, contact_id, group_id):
        wd = self.app.wd
        self.open_page()
        self.select_contact_by_id(contact_id)
        wd.find_element_by_name("to_group").find_element_by_css_selector("[value='%s']" % group_id)
        wd.find_element_by_name("add").click()

    def select_contact_by_id(self, id):
        wd = self.app.wd
        self.open_page()
        wd.find_element_by_css_selector("input[value='%s']" % id).click()


    def view_contact_from_group(self, group_id):
        wd = self.app.wd
        self.open_page()
        wd.find_element_by_name("group").find_element_by_css_selector("[value='%s']" % group_id).click()


    def delete_contact_from_group(self, contact_id):
        wd = self.app.wd
        wd.find_element_by_css_selector("input[value='%s']" % contact_id).click()
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to.alert.accept()
        wd.find_element_by_css_selector("div.msgbox")