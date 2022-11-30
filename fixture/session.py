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

    def ensure_Logout(self):
        wd = self.app.wd
        if self.is_logged_in():
            self.Logout()

    def is_logged_in(self):
        wd = self.app.wd
        return len(wd.find_elements_by_link_text("Logout")) > 0

    def ensure_Login(self, username, password):
        wd = self.app.wd
        if self.is_logged_in():
            if self.is_logged_in_as(username):
                return
            else:
                self.Logout()
        self.Login(username, password)

    def is_logged_in_as(self, username):
        wd = self.app.wd
        return self.get_logged_user() == username
    def get_logged_user(self):
        wd = self.app.wd
        return wd.find_element_by_xpath("//div[1]/form/b").text[1:-1]
