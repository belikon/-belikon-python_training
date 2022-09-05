# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re
from group import Group
from application import Application
import pytest

@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_add_group(app):
    app.Login(username="admin", password="secret")
    app.create_group(Group(group_name="test", group_header="test logo", group_footer="test group"))
    app.logout()

def test_add_empty_group(app):
    app.Login(username="admin", password="secret")
    app.create_group(Group(group_name="", group_header="", group_footer=""))
    app.logout()

