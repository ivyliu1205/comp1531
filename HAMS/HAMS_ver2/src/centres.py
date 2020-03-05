from abc import ABC

class Centres(ABC):

    def __init__(self, name, suburb, service, ratings, opening_time):
      self._name = name
      self._suburb = suburb
      self._providers = []
      self._service = service
      self._ratings = ratings
      self._opening_time = opening_time
      self._bookings = []

    def get_name(self):
        return self._name


    def get_suburb(self, period):
        return self._suburb

    def get_providers(self):
        return self._providers

    def __str__(self):
        return "Centre details: {0}".format(self._name)

    def get_service(self):
        return self._service
        
    def get_ratings(self):
        return self._ratings
        
    def get_opening_time(self):
        return self._opening_time
        
    def get_bookings(self):
        return self._bookings

    def add_booking(self, booking):
        self._bookings.append(booking)
        
    def add_provider(self,provider):
        self._providers.append(provider)
    
    def add_service(self,provider):
        self._service.append(service)
        
    
