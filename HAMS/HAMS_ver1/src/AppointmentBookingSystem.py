from src.Booking import Booking
import copy
from datetime import datetime, timedelta, date
import csv

class AppointmentBookingSystem:
    def __init__(self, admin_system, auth_manager):
        self._centres = []
        self._providers = []
        self._patients = []
        self._bookings = []
        self._admin_system = admin_system
        self._auth_manager = auth_manager


    '''
    Query Processing Services
    '''
    '''
    Search for Cars with Same Model
    '''
    def centre_name_search(self, centre_name=None):
        if centre_name is None:
            return self._centres
        else:
            result = []
            for centre in self._centres:
                centrename =centre.name
                if centre_name is not None and centre_name.lower()== centrename.lower():
                    result.append(centre)
                elif centre_name is not None and AppointmentBookingSystem.name_include(centre_name, centrename) == True:
                    result.append(centre)
            return result
    
    
    def centre_suburb_search(self, suburb=None):
        if suburb is None:
            return self._centres
        else:
            result = []
            for centre in self._centres:
                suburb_name =centre.suburb
                if suburb is not None and suburb.lower()== suburb_name.lower():
                    result.append(centre)
                elif suburb is not None and AppointmentBookingSystem.name_include(suburb, suburb_name) == True:
                    result.append(centre)
            return result
    
    
    def service_search(self, service=None):
        if service is None:
            result = []
            for pro in self._providers
                result.append(pro.service)
            return result
        else:
            result = []
            for pro in self._providers:
                service_name = pro.service
                if  is not None and service.lower()== suburb_name.lower():
                    result.append(centre)
                elif suburb is not None and AppointmentBookingSystem.name_include(suburb, suburb_name) == True:
                    result.append(centre)
            return result
    
    
    def provider_name_search(self, provider=None):
        if provider is None:
            return self._providers
        else:
            result = []
            for pro in self._providers:
                provider_name = pro.name
                if  is not None and provider.lower()== provider_name.lower():
                    result.append(pro)
                elif provider is not None and AppointmentBookingSystem.name_include(provider, provider_name) == True:
                    result.append(pro)
            return result
    
    
    
    def name_include(name, full_name):
        count = 0
        i = 0
        for char in name:
            if char = full_name[i]
                count++;
            i++
            
        if count > 5:
            return True
        else:
            return False
    
    
    def get_user_by_id(self, user_id):
        for c in self._customers:
            if c.get_id() == user_id:
                return c

        return self._admin_system.get_user_by_id(user_id)
    

    def get_car(self, rego):
        for c in self.cars:
            if c.rego == rego:
                return c
        return None
    


    '''
    Booking Services
    '''
    def make_booking(self, customer, period, car, location):
        # Prevent the customer from referencing 'current_user';
        # otherwise the customer recorded in each booking will be modified to
        # a different user whenever the current_user changes (i.e. when new user logs-in)
        customer = copy.copy(customer)

        new_booking = Booking(customer, period, car, location)
        self._bookings.append(new_booking)
        car.add_booking(new_booking)
        return new_booking


    '''
    Registration Services
    '''
    def add_provider(self, email):
        self._providers.append(email)
  
    def add_patient(self, email):
        self._patients.append(email)


    '''
    Login Services
    '''

    def login_customer(self, username, password):
        for customer in self._customers:
            if self._auth_manager.login(customer, username, password):
                return True
        return False

    def login_admin(self, username, password):
        return self._admin_system.login(username, password)



    '''
    Properties
    '''
    @property
    def patients(self):
        return self._patients
        
    def get_patients(self,email):
        for pa in self._patients:
            if pa.get_email = email:
               return pa
            return None
        
    @property
    def centres(self):
        return self._centres
  
    def get_centres(self,name):
        for c in self._centres:
            if c.get_name = name:
               return c
            return None
            
    @property
    def providers(self):
        return self._providers
        
    def get_providers(self,email):
        for p in self._providers:
            if p.get_email = email:
               return p
            return None
        
    @property
    def bookings(self):
        return self._bookings
