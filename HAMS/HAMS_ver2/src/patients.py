from abc import ABC

class Patient(ABC):

    def __init__(self, email, name):
      self.email = email
      self.name = name

    def get_email(self):
        return self._email
        
    def get_name(self):
        return self._name

    def __str__(self):
        return "Patient details: {0}".format(self._name)

