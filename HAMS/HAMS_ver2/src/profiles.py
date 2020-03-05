#View providers' & centres'
import csv

class provider:
   def __init__(self,email):
      self.email = email
      self.name = []
      self.phone = []
      self.ratings = []
      self.types = []
      self.service = []
      
   def view_profile(self,email):
      with open('provider.csv','r') as provider_file:
         pro_file = csv.reader(provider_file)
         
      for row in pro_file:
         if row[1] == self.email
            _name = row[0]
            _phone = row[3]
            _ratings = row[6]
            _types = row[2]
            self.name.append(_name)
            self.phone.append(_phone)
            self.ratings.append(_ratings)
            self.types.append(_types)
            
    def working_hospital(self,email):
       with open('provider_health_centres.csv','r') as provider_file:
          pro_file = csv.reader(provider_file)
         
       for row in pro_file:
          if row[0] = self.email
             self.service.append(row[1])
     
class centre:
   def __init__(self,name):
      self.name = name
      self.abn = []
      self.suburb = []
      self.phone = []
      self.service = []
      self.ratings = [] 
      self.opening_time = []
      
   def view_profile(self,name):
      with open('health_centres.csv','r') as centre_file:
         cen_file = csv.reader(centre_file)
         
      for row in cen_file:
         if row[2] == self.name
            _abn = row[2]
            _suburb = row[4]
            _phone = row[3]
            _service = row[0]
            _ratings = row[6] 
            _opening_time = [5]
            self.abn.append(_abn)
            self.suburb.append(_suburb)
            self.phone.append(_phone)
            self.service.append(_service)
            self.ratings.append(_ratings)
            self.opening_time.append(_opening_time)
            
class patient:
   def __init__(self,email):
      self.email = email
      self.name = []
      
   def view_profile(self,name):
      with open('patient.csv','r') as patient_file:
         pat_file = csv.reader(patient_file)
         
      for row in cen_file:
         if row[1] == self.email
            self.name.append(row[0])
      
