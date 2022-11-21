from model.group import Group
class GroupHelper:

    def __init__(self, app):
        self.app = app


    def create(self, group):
        wd = self.app.wd
        self.open_groups_page()
        # init add group
        wd.find_element_by_name("new").click()
        # fill group form
        self.fill_group_form(group)
        # submit group creation
        wd.find_element_by_name("submit").click()

    def fill_group_form(self, group):
        wd = self.app.wd
        self.change_field_value("group_name", group.group_name)
        self.change_field_value("group_header", group.group_header)
        self.change_field_value("group_footer", group.group_footer)

    def change_field_value(self, field_name, test):
        wd = self.app.wd
        if test is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(test)

    def open_groups_page(self):
        wd = self.app.wd
        if (wd.current_url == "http://localhost/addressbook/group.php" and len(wd.find_elements_by_name("new")) > 0):
            return
        wd.find_element_by_link_text("groups").click()

    def delete_first_group(self):
        wd = self.app.wd
        self.open_groups_page()
        # select first group
        self.select_first_group()
        # submit deletion
        wd.find_element_by_name("delete").click()
        #wd.find_element_by_link_text("group page").click()


    def test_edit_first_group(self, group):
        wd = self.app.wd
        self.open_groups_page()
        # select first group
        self.select_first_group()
        wd.find_element_by_name("edit").click()
        self.fill_group_form(group)
        wd.find_element_by_name("update").click()
        #wd.find_element_by_link_text("group page").click()

    def test_edit_first_group_name(self, new_group_data):
        wd = self.app.wd
        self.open_groups_page()
        self.select_first_group()
        wd.find_element_by_name("edit").click()
        self.fill_group_form(new_group_data)
        wd.find_element_by_name("update").click()
        #wd.find_element_by_link_text("group page").click()

    def select_first_group(self):
        wd = self.app.wd
        # select first group
        wd.find_element_by_name("selected[]").click()

    def count(self):
        wd = self.app.wd
        self.open_groups_page()
        return len(wd.find_elements_by_name("selected[]"))

    def get_group_list(self):
        wd = self.app.wd
        self.open_groups_page()
        groups = []
        for element in wd.find_elements_by_css_selector("span.group"):
            text = element.text
            id = element.find_element_by_name("selected[]").get_attribute("value")
            groups.append(Group(group_name = text, id = id))
        return groups

