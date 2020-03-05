from abc import ABC

class Provider(ABC):

    def __init__(self, email, name, phone, ratings, types, service):
      self.email = email
      self.name = name
      self.phone = phone
      self.ratings = ratings
      self.types = types
      self.service = service

    def get_email(self):
        return self._email
        
    def get_name(self):
        return self._name

    def get_phone(self):
        return self._phone

    def __str__(self):
        return "Provider details: {0}".format(self._name)

    def get_ratings(self):
        return self._ratings
        
    def get_types(self):
        return self._types
        
    def get_service(self):
        return self._service
        
    def get_bookings(self):
        return self._bookings

