from sqlalchemy.inspection import inspect
from application.enums import UserRole

class Serializer(object):

    def serialize(self):
        dictionary = {}
        for c in inspect(self).attrs.keys():
          if (isinstance(getattr(self, c), UserRole)):
            dictionary[c] = getattr(self, c).name
          else:
            dictionary[c] = getattr(self, c)
        return dictionary

    @staticmethod
    def serialize_list(l):
        return [m.serialize() for m in l]
