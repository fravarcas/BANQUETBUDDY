from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Particular, CateringCompany, Employee


class ParticularForm(forms.ModelForm):
    class Meta:
        model = Particular
        fields = ['phone_number', 'preferences', 'address', 'is_subscribed']

class CateringCompanyForm(forms.ModelForm):
    class Meta:
        model = CateringCompany
        fields = ['name', 'phone_number', 'service_description', 'cuisine_type', 'is_verified', 'price_plan']

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['phone_number', 'profession', 'experience', 'skills', 'location']