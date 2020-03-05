    
'''Group Project__TEAM 1'''
'''Import'''
from flask import render_template, request, redirect, url_for, abort
from flask_login import login_required, current_user
from src.AppointmentBookingSystem import AppointmentBookingSystem
from server import app, auth_manager
from datetime import datetime
import csv

'''Functions'''
#Main Page
@app.route('/')
def home():
    return render_template('home.html')

#Login
@app.route('/login', methods=['GET', 'POST'])
def login():
    print('Welcome to the eHealth program, please sign in')
    
    
    Email = request.form["Email"]
    Password = request.form["Password"]
    with open ('provider.csv') as pro:
        pro_reader = csv.DictReader(pro)
        database1 = []
        for row in pro_reader:
            database1.append(dict(provider_email=row['provider_email'],
                                provider_type=row['provider_type'],
                                password=row['password']))
    with open ('patient.csv') as pat:
        pat_reader = csv.DictReader(pat)
        database2 = []
        for row in pat_reader:
            database2.append(dict(patient_email = row['patient_email'],
                                  password = row['password']))
        
    
    
    logEmail = False
    logPassword = False
    while logEmail != True and logPassword != True:
        
        for row in database1:
            Pro_Email_File = row['provider_email']
            Pro_Password_File = row['password']
            if (Pro_Email_File == Email and
                Password_File == Password):
                logEmail = True
                logPassword = True
                redir = request.args.get('next')
                return redirect(redir or url_for('home'))
            elif (Pro_Email_File == Email and Password_File != Password):
                logEmail = True
                
        for row in database2:
            Pat_Email_File = row['patient_email']
            Pat_Password_File = row['password']
            if (Pat_Eamil_File == Email and
                Pat_Password_File == Password):
                logEmail = True
                logPassword = True
                redir = request.args.get('next')
                return redirect(redir or url_for('home'))
            elif (Pat_Email_File == Email and Pat_Password_File != Password):
                logEmail = True
            
        if logEmail is not True:
            return render_template('login.html')
        elif logPassword is not True:
            return render_template('login.html')


#Register
@app.route('/register', methods=['GET', 'POST'])
def register():
    '''
    Complete this function
    '''
    
#Logout   
@app.route('/logout')
@login_required
def logout():
    auth_manager.logout()
    return redirect(url_for('home'))
   
#Error Page
@app.route('/404')
@app.errorhandler(404)
def page_not_found(e=None):
    return render_template('404.html'), 404

#Book Appointments
@app.route('/book_appointments')
@login_required
def book_appointments(): 
    '''
    Complete this function
    '''    

#Future Appointments
@app.route('/future_appointments')
@login_required
def appointments(): 
    '''
    Complete this function
    '''
         
#Appointment history of patients
@app.route('/history')
@login_required
def history():
    '''
    Complete this function
    '''
    
#Search for healthcare center and providers
@app.route('/search', methods=['GET', 'POST'])
@login_required
def search(): 
    '''
    Complete this function
    '''
    #search for a health centre
    centre_name = request.args.get("centre_name")
    if centre_name is None:
        centre_name = None
    centre = system.centre_name_search(centre_name)
    return render_template('search.html', centre = centre)
    
    #search for a health provider
    centre_suburb = request.args.get("centre_suburb")
    if centre_suburb is None:
        centre_suburb = None
    centre = system.centre_suburb_search(centre_suburb)
    return render_template('search.html', centre = centre)
    
    #search for a type of service
    service = request.args.get("service")
    if service is None:
        service = None
    centre = system.service_search(service)
    return render_template('search.html', centre = centre)
    
    
    #search for a health-care provider by name
    provider_name = request.args.get("provider_name")
    if provider_name is None:
        provider_name = None
    provider = system.provider_name_search(provider_name)
    return render_template('search.html', provider = provider)

#View provider profile
@login_required
def view_providers(email):
    providers = system.get_providers(email)
    if providers is None:
        abort(404)
    return render_template('provider_details.html', providers=providers)

#View centre profile
@login_required
def view_centres(name): 
    centres = system.get_centres(name)
    if centres is None:
        abort(404)
    return render_template('centre_details.html', centres=centres)
    
#View patient profile
@login_required
def view_patient(email): 
    patients = system.get_patients(email)
    if patients is None:
        abort(404)
    return render_template('patient_details.html', patients=patients)

    

#Future Appointments of health providers
@app.route('/future_appointments_pro')
@login_required
def appointments_pro(): 
    '''
    Complete this function
    '''
    
#Appointment history of health providers
@app.route('/history_pro')
@login_required
def history_pro():
    '''
    Complete this function
    '''
    
#Taking Notes
@app.route('/take_notes')
@login_required
def take_notes(email):
    patients = system.get_patients(email)
    if patients is None:
        abort(404)
    return render_template('taking_notes.html', patients=patients)

    
