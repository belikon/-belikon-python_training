# -*- coding: utf-8 -*-
from model.contact import Contact
import pytest
import random
import string
import jsonpickle
import getopt
import sys
import os

try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of contact", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 5
f = "data/contacts.json"

for o,a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a

def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

testdata = [Contact(abon_first_name="", abon_middle_name="", abon_last_name="", address = "",
            phone_home = "", phone_mobile = "", phone_work = "", secondaryphone = "",
            email = "", email2 = "", email3 = "" )] + [
    Contact(abon_first_name=random_string("abon_first_name", 10),
            abon_middle_name=random_string("abon_middle_name", 20),
            abon_last_name=random_string("abon_last_name", 20),
            address=random_string("address", 20),
            phone_home=random_string("phone_home", 20),
            phone_mobile=random_string("phone_mobile", 20),
            phone_work=random_string("phone_work", 20),
            secondaryphone=random_string("secondaryphone", 20),
            email=random_string("email", 20), email2=random_string("email2", 20), email3=random_string("email3", 20))
    for i in range(n)
]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file, "w") as out:
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(testdata))