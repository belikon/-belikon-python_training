from sys import maxsize
class Contact:
    def __init__(self, abon_first_name = None, abon_middle_name = None, abon_last_name = None, abon_nikname = None,
                 company = None, address = None, title = None,
                 phone_home = None, phone_mobile = None, phone_work = None, secondaryphone = None,
                 email = None, email2 = None, email3 = None, secondary_address = None, homepage = None, id = None, all_phones_from_home_page = None, all_email_from_home_page = None):

        self.abon_first_name = abon_first_name
        self.abon_middle_name = abon_middle_name
        self.abon_last_name = abon_last_name
        self.abon_nikname = abon_nikname

        self.company = company
        self.address = address
        self.title = title

        self.phone_home = phone_home
        self.phone_mobile = phone_mobile
        self.phone_work = phone_work
        self.secondaryphone = secondaryphone

        self.email = email
        self.email2 = email2
        self.email3 = email3
        self.secondary_address = secondary_address
        self.homepage = homepage

        self.id = id
        self.all_phones_from_home_page = all_phones_from_home_page
        self.all_email_from_home_page = all_email_from_home_page

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize
    def __repr__(self):
        return "%s:%s:%s;%s;%s;%s;%s;%s;%s;%s;%s" % (self.id, self.abon_first_name, self.abon_last_name, self.address, self.phone_home, self.phone_mobile, self.phone_work,
                             self.secondaryphone, self.email, self.email2, self.email3)


    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and \
               (self.abon_first_name is None or other.abon_first_name is None or self.abon_first_name == other.abon_first_name) and \
               (self.abon_last_name is None or other.abon_last_name is None or self.abon_last_name == other.abon_last_name)