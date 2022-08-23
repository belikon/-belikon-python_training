# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re
from group import Group

class TestAddGroup(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)

    def open_URL(self, wd):
        # open URL
        wd.get("http://localhost/addressbook/")

    def Login(self, wd, username, password):
        # login+password
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_id("LoginForm").submit()

    def logout(self, wd):
        # logout
        wd.find_element_by_link_text("Logout").click()

    def create_group(self, wd, group):
        # init add group
        wd.find_element_by_name("new").click()
        # fill group form
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(group.group_name)
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys(group.group_header)
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys(group.group_footer)
        # submit group creation
        wd.find_element_by_name("submit").click()
        wd.find_element_by_id("container").click()

    def open_groups_page(self, wd):
        # open groups page
        wd.find_element_by_link_text("groups").click()

    def test_add_group(self):
        wd = self.wd
        self.open_URL(wd)
        self.Login(wd, username="admin", password="secret")
        self.open_groups_page(wd)
        self.create_group(wd, Group(group_name="test", group_header="test logo", group_footer="test group"))
        self.logout(wd)

    def test_add_empty_group(self):
        wd = self.wd
        self.open_URL(wd)
        self.Login(wd, username="admin", password="secret")
        self.open_groups_page(wd)
        self.create_group(wd, Group(group_name="", group_header="", group_footer=""))
        self.logout(wd)
    def is_element_present(self, how, what):
        try: self.wd.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.wd.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    def tearDown(self):
        self.wd.quit()

if __name__ == "__main__":
    unittest.main()