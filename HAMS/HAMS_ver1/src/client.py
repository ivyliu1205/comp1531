'''
write down for the some providers and patients here
'''
from .AppointmentBookingSystem import AppointmentBookingSystem
from .AdminSystem import AdminSystem
from .AuthenticationManager import AuthenticationManager
import .Provider 
import .Patient
import .Centre


def bootstrap_system(auth_manager):

    admin_system = AdminSystem(auth_manager)
    system = OnlineSystem(admin_system, auth_manager)

    return system
