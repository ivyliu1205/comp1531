from abc import ABC


class Provider(ABC):

    def __init__(self, provider_num, name, curr_rating):
        self._provider_num  = provider_num
        self._name = name
        self._curr_rating = curr_rating
        self._service = []
        self._centres = []
        self._period = []
        self._bookings = []

    
    
    @property
    def name(self):
        return self._name
    
    @property
    def provider_num(self):
        return self._provider_num

    @property
    def curr_rating(self):
        return self._curr_rating
    
    @property
    def service(self):
        return self._service
    
    @property
    def centres(self):
        return self._centres
    
    @property
    def bookings(self):
        return self._bookings
    
    @property
    def period(self):
        return self._period
    
    
    @property
    def add_period(self, period):
        self._period.append(period)
    
    @property
    def add_service(self, service):
        self._service.append(service)
        
    @property
    def add_centres(self, centre):
        self._centres.append(centre)
    
    @property
    def add_booking(self, booking):
        self._bookings.append(booking)
    

    
    def __str__(self):
        return f'Provider <{self.name}, {self.provider_num}>'


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
