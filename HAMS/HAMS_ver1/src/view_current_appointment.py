from book_an_appointment import book
from flask import request, render_template


#get new appointment from patient who booked appointment

@app.route('/', methods=['POST', 'GET'])
def appointment(Name):
    if request.method == 'POST':
        Appointment_type = request.form["GPdoctor"]
        starts = book.starttime()
        ends = book.endtime()
        patient = book.email()
        fee = float(ends-starts)*1.5
        
        return render_template('current_appointment.html', Appointment_type = Appointment_type, starts = starts, ends = ends, patient = patient, fee = fee)
    return render_template('current_appointment.html')
