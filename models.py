from google.appengine.ext import ndb

class Pet(ndb.Model):
    name =  ndb.StringProperty(required=True)
    difficulty =  ndb.StringProperty(required=True)
    food =  ndb.StringProperty(required=True)
    need1 =  ndb.StringProperty(required=True)
    need2 =  ndb.StringProperty(required=False)
