from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import ParticularForm, CateringCompanyForm, EmployeeForm

def home(request):
    return render(request, 'core/home.html')

def about_us(request):
    return render(request, 'core/aboutus.html')
  
def subscription_plans(request):
    return render(request, 'core/subscriptionsplans.html')
  
def faq(request):
    return render(request, 'core/faq.html')

def contact(request):
    return render(request, 'core/contact.html')

def register_particular(request):
    if request.method == 'POST':
        user_form = UserCreationForm(request.POST)
        particular_form = ParticularForm(request.POST)

        if user_form.is_valid() and particular_form.is_valid():
            # Crear el usuario
            user = user_form.save()

            # Crear el perfil particular asociado
            particular_profile = particular_form.save(commit=False)
            particular_profile.user = user
            particular_profile.save()

            # Redirigir a la página de registro exitoso u otra página
            return redirect('registro_exitoso')

    else:
        user_form = UserCreationForm()
        particular_form = ParticularForm()

    return render(request, 'core/registro_particular.html', {'user_form': user_form, 'particular_form': particular_form})
