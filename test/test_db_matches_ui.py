from model.group import Group
from model.contact import Contact

from timeit import timeit

def test_group_list(app, db):
    ui_list = app.group.get_group_list()
    def clean(group):
        return Group(id=group.id, group_name=group.group_name.strip())
    db_list = map(clean, db.get_group_list())
    assert sorted(ui_list, key=Group.id_or_max) == sorted(db_list, key=Group.id_or_max)

def test_group_list_time(app, db):
   print(timeit(lambda: app.group.get_group_list(), number=1))
   print(timeit(lambda: db.get_group_list(), number=1000))
   assert False

