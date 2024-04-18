from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import ServiceRequest

class ServiceRequestForm(forms.ModelForm):
    GAS_LEAK_DETECTION = 'Gas Leak Detection and Repair'
    NEW_CONNECTION_INSTALLATION = 'New Gas Connection Installation'
    APPLIANCE_INSTALLATION_OR_REPAIR = 'Gas Appliance Installation or Repair'
    METER_INSTALLATION_OR_REPAIR = 'Meter Installation, Replacement, or Repair'
    GAS_PRESSURE_TESTING = 'Gas Pressure Testing'
    SERVICE_INTERRUPTION = 'Gas Service Interruption'
    GAS_ODOR_INVESTIGATION = 'Gas Odor Investigation'
    BILLING_AND_ACCOUNT_INQUIRY = 'Billing and Account Inquiry'
    EMERGENCY_RESPONSE = 'Emergency Response'
    ENERGY_EFFICIENCY_PROGRAMS = 'Energy Efficiency Programs'

    REQUEST_TYPES = [
        (GAS_LEAK_DETECTION, 'Gas Leak Detection and Repair'),
        (NEW_CONNECTION_INSTALLATION, 'New Gas Connection Installation'),
        (APPLIANCE_INSTALLATION_OR_REPAIR, 'Gas Appliance Installation or Repair'),
        (METER_INSTALLATION_OR_REPAIR, 'Meter Installation, Replacement, or Repair'),
        (GAS_PRESSURE_TESTING, 'Gas Pressure Testing'),
        (SERVICE_INTERRUPTION, 'Gas Service Interruption'),
        (GAS_ODOR_INVESTIGATION, 'Gas Odor Investigation'),
        (BILLING_AND_ACCOUNT_INQUIRY, 'Billing and Account Inquiry'),
        (EMERGENCY_RESPONSE, 'Emergency Response'),
        (ENERGY_EFFICIENCY_PROGRAMS, 'Energy Efficiency Programs'),
    ]

    request_type = forms.ChoiceField(choices=REQUEST_TYPES)
    details = forms.CharField(widget=forms.Textarea)
    attachment = forms.FileField(required=False)

    class Meta:
        model = ServiceRequest
        fields = ['request_type', 'details', 'attachment']

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
