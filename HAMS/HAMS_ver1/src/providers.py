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

class GP(Provider):

    def __init__(self, nane, provider_num, curr_rating):
        super().__init__(name, provider_num, curr_rating, 50)

    def __str__(self):
        return f'GP <{self.name}, {self.curr_rating}>'



class Pharmacist(Provider):
    def __init__(self, name, provider_num, curr_rating):
        super().__init__(name, provider_num, curr_rating, 75)

    def __str__(self):
        return f'Pharmacist <{self.name}, {self.curr_rating}>'



class Physiotherapist(Provider):
    def __init__(self, name, provider_num, curr_rating):
        super().__init__(name, provider_num, curr_rating, 100)

    def __str__(self):
        return f'Physiotherapist <{self.name}, {self.curr_rating}>'



class Pathologist(Provider):

    def __init__(self, name, provider_num, curr_rating):
        super().__init__(name, provider_num, curr_rating, 150)

    def __str__(self):
        return f'Pathologist <{self.name}, {self.curr_rating}>'
