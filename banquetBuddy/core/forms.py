from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Particular, CateringCompany, Employee


class ParticularForm(forms.ModelForm):
    class Meta:
        model = Particular
        fields = ['phone_number', 'preferences', 'address']
        widgets = {
            'phone_number': forms.TextInput(attrs={'placeholder': 'Número de teléfono', 'class': 'rounded-input'}),
            'preferences': forms.TextInput(attrs={'placeholder': 'Preferencias', 'class': 'rounded-input'}),
            'address': forms.TextInput(attrs={'placeholder': 'Dirección', 'class': 'rounded-input'}),
        }

class CateringCompanyForm(forms.ModelForm):
    class Meta:
        model = CateringCompany
        fields = ['name', 'phone_number', 'service_description']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Nombre', 'class': 'rounded-input'}),
            'phone_number': forms.TextInput(attrs={'placeholder': 'Número de teléfono', 'class': 'rounded-input'}),
            'service_description': forms.TextInput(attrs={'placeholder': 'Descripción del servicio', 'class': 'rounded-input'}),
        }

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['phone_number', 'profession', 'experience', 'skills']
        widgets = {
            'phone_number': forms.TextInput(attrs={'placeholder': 'Número de teléfono', 'class': 'rounded-input'}),
            'profession': forms.TextInput(attrs={'placeholder': 'Profesión', 'class': 'rounded-input'}),
            'experience': forms.TextInput(attrs={'placeholder': 'Experiencia', 'class': 'rounded-input'}),
            'skills': forms.TextInput(attrs={'placeholder': 'Habilidades', 'class': 'rounded-input'}),
        }

class StyledUserCreationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(StyledUserCreationForm, self).__init__(*args, **kwargs)
        for fieldname in ['username', 'password1', 'password2']:
            self.fields[fieldname].help_text = None
            self.fields[fieldname].widget.attrs.update({'class': 'rounded-input', 'placeholder': self.fields[fieldname].label})
