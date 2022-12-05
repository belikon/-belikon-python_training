from model.group import Group
import random
import string

testdata = [
    Group(group_name="name1", group_header="header1", group_footer="footer1"),
    Group(group_name="name2", group_header="header2", group_footer="footer2")
]
'''
def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

#testdata = [
#    Group(group_name=name, group_header=header, group_footer=footer)
#    for name in ["", random_string("name", 10)]
#    for header in ["", random_string("header", 20)]
#    for footer in ["", random_string("footer", 20)]
#     ]

testdata = [Group(group_name="", group_header="", group_footer="")] + [
    Group(group_name=random_string("name", 10), group_header=random_string("header", 20), group_footer=random_string("footer", 20))
    for i in range(5)
]
'''