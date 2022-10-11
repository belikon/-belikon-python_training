
def test_delete_first_contact(app):
    app.session.Login(username="admin", password="secret")
    app.contact.test_delete_first_contact()
    app.session.Logout()