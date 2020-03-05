class Booking(object):

    def __init__(self, customer, date, time, healthProvider, healthcareCentre):
        self._customer = customer
        self._date = date
        self._time = time
        self._healthProvider = healthProvider
        self._healthcareCentre = healthcareCentre

  
    @property
    def healthProvider(self):
        return self._healthProvider
    
    @property
    def healthcareCentre(self):
        return self._healthcareCentre

    def __str__(self):
        return "Booking for: {}, {}".format(self._customer, self._healthProvider)


