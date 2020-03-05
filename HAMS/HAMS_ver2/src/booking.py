import csv
from flask import render_template


SLOT_1 = '8:00AM'
SLOT_2 = '8:30AM'
SLOT_3 = '9:00AM'
SLOT_4 = '9:30AM'
SLOT_5 = '10:00AM'
SLOT_6 = '10:30AM'
SLOT_7 = '11:00AM'
SLOT_8 = '11:30AM'
SLOT_9 = '1:00PM'
SLOT_10 = '1:30PM'
SLOT_11 = '2:00PM'
SLOT_12 = '2:30PM'
SLOT_13 = '3:00PM'
SLOT_14 = '3:30PM'
SLOT_15 = '4:00PM'
SLOT_16 = '4:30PM'
SLOT_17 = '5:00PM'
SLOT_18 = '5:30PM'
SLOT_19 = '6:00PM'

class Patients(object):

    def __init__(self, first_name, last_name, ssn):
        self.first_name = first_name
        self.last_name = last_name
        self.ssn = ssn
        self.patients_name = self.f_name + " " + self.l_name
        self.patients_id = self.f_name[:1] + self.l_name + ssn
        self.patients_calendar = {
            CLASS_NAME: self.patients_name,
            self.CLASS_ID: self.patients_id,
            CLASS_APPOINTMENT_INFO: {}
        }
    def get_patients_record(self):
        patient_record =  {
            CLASS_NAME : self.patients_name,
            self.CLASS_ID : self.patients_id,
        }
        return patients_record

    def print_patients_calendar(self):
         print self.patients_calendar
         
class HealthCareProviders(object):

    def __init__(self, first_name, last_name, spec):
        self.first_name = first_name
        self.last_name = last_name
        self.HealthCareProviders_name = self.first_name + " " + self.last_name
        self.spec = spec
        self.HealthCareProviders_calendar = {
            CLASS_NAME: self.HealthCareProviders_name,
            self.CLASS_SPEC: self.spec,
            CLASS_APPOINTMENT_INFO: {},
        }

    def get_HealthCareProviders_record(self):
        HealthCareProviders_record =  {
            CLASS_NAME : self.HealthCareProviders_name,
            self.CLASS_SPEC: self.spec
        }
        return HealthCareProviders_record

    def print_HealthCareProviders_calendar(self):
        print self.HealthCareProviders_calendar

class Appointments(object):

    def schedule(self,HealthCareProviders,patient,time):
        self.time = time
        self.HealthCareProviders = HealthCareProviders
        self.patient = patient
        if self.isHealthCareProvidersavailable(HealthCareProviders,time) 
            self.update_HealthCareProviders_calendar(patient,HealthCareProviders,time)
            return True

    def isHealthCareProvidersavailable(self,HealthCareProviders,time):
        if HealthCareProviders.HealthCareProviders_calendar[CLASS_APPOINTMENT_INFO].has_key(time):
            print "Sorry, No Appointment Available\n"
            return False else:
            return True

 

    def update_HealthCareProviders_calendar(self,patient,doctor,time):
        HealthCareProviders.HealthCareProviders_calendar[CLASS_APPOINTMENT_INFO][time] = patient.get_patient_record()
