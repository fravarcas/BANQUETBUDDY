from django import forms
from django.contrib.auth.forms import AuthenticationForm

class EmailAuthenticationForm(AuthenticationForm):
    username = forms.EmailField(
        widget=forms.TextInput(attrs={'autofocus': True, 'placeholder': 'Email', 'class': 'rounded-input'})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Contraseña', 'class': 'rounded-input'})
    )