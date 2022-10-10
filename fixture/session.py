class SessionHelper:

    def __init__(self, app):
        self.app = app

    def Login(self, username, password):
        wd = self.app.wd
        # open URL
        wd.get("http://localhost/addressbook/")
        # login+password
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_id("LoginForm").submit()

    def Logout(self):
        wd = self.app.wd
        wd.find_element_by_link_text("Logout").click()
        wd.find_element_by_name("user")