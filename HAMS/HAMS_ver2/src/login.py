import csv
from flask import request, render_template


def login():
    print('Welcome to the eHealth program, please sign in')
    
    logEmail = False
    logPassword = False
    while logEmail != True and logPassword != True:
        Username = request.form["Email"]
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
        
        
        
        
        for row in database1:
            Pro_Email_File = row['provider_email']
            Provider_type_File = row['provider_type']
            Pro_Password_File = row['password']
            if (Pro_Email_File == Email and
                Password_File == Password):
                logEmail = True
                logPassword = True
                return render_template('login.html')
            elif (Pro_Email_File == Email and Password_File != Password):
                logEmail = True
                
        for row in database2:
            Pat_Email_File = row['patient_email']
            Pat_Password_File = row['password']
            if (Pat_Eamil_File == Email and
                Pat_Password_File == Password):
                logEmail = True
                logPassword = True
                return render_template('login.html')
            elif (Pat_Email_File == Email and Pat_Password_File != Password):
                logEmail = True
            
        if logEmail is not True:
            print ('Wrong Eamil')
        elif logPassword is not True:
            print('Wrong Password')

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})


