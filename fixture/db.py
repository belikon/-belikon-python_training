import pymysql.cursors
from model.group import Group
from model.contact import Contact

class DbFixture:
    def __init__(self, host, name, user, password):
        self.host = host
        self.name = name
        self.user = user
        self.password = password
        self.connection = pymysql.connect(host=host, database=name, user=user, password=password, autocommit=True)

    def get_group_list(self):
        list=[]
        cursor = self.connection.cursor()
        try:
            cursor.execute("select group_id, group_name, group_header, group_footer from group_list")
            for row in cursor:
                (id, name, header, footer) = row
                list.append(Group(id = str(id), group_name=name, group_header=header, group_footer=footer))
        finally:
            cursor.close()
        return list
    def destroy(self):
        self.connection.close()

    def get_contact_list(self):
        list=[]
        cursor = self.connection.cursor()
        try:
            cursor.execute("select id, firstname, lastname, address, home, mobile, work, phone2, email, email2, email3 from addressbook where deprecated='0000-00-00 00:00:00'")
            for row in cursor:
                (id, firstname, lastname, address, home, mobile, work, phone2, email, email2, email3) = row
                list.append(Contact(id = str(id), abon_first_name=firstname, abon_last_name=lastname, address = address,
                                    phone_home = home, phone_mobile=mobile, phone_work=work, secondaryphone=phone2,
                                    email=email, email2=email2, email3=email3))
        finally:
            cursor.close()
        return list
    def destroy(self):
        self.connection.close()

