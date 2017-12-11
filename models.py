from google.appengine.ext import ndb


class Guest(ndb.Model):
    guest_name = ndb.StringProperty()
    guest_email = ndb.StringProperty()
    guest_phone_number = ndb.StringProperty()
    guest_message = ndb.StringProperty()
