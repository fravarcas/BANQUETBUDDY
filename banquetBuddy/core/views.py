from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import ParticularForm, CateringCompanyForm, EmployeeForm, StyledUserCreationForm

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
            
            user = user_form.save()

            particular_profile = particular_form.save(commit=False)
            particular_profile.user = user
            particular_profile.save()

            
            return redirect('home')

    else:
        user_form = StyledUserCreationForm()
        particular_form = ParticularForm()

    return render(request, 'core/registro_particular.html', {'user_form': user_form, 'particular_form': particular_form})

def register_employee(request):
    if request.method == 'POST':
        user_form = UserCreationForm(request.POST)
        employee_form = EmployeeForm(request.POST)

        if user_form.is_valid() and employee_form.is_valid():
            
            user = user_form.save()

            employee_profile = employee_form.save(commit=False)
            employee_profile.user = user
            employee_profile.save()
            
            return redirect('home')

    else:
        user_form = StyledUserCreationForm()
        employee_form = EmployeeForm()

    return render(request, 'core/registro_empleado.html', {'user_form': user_form, 'employee_form': employee_form})

def register_company(request):
    if request.method == 'POST':
        user_form = UserCreationForm(request.POST)
        company_form = CateringCompanyForm(request.POST)

        if user_form.is_valid() and company_form.is_valid():
            
            user = user_form.save()

            company_profile = company_form.save(commit=False)
            company_profile.user = user
            company_profile.save()
            
            return redirect('home')

    else:
        user_form = UserCreationForm()
        company_form = CateringCompanyForm()

    return render(request, 'core/registro_company.html', {'user_form': user_form, 'company_form': company_form})


def elegir_registro(request):
    return render(request, 'core/elegir_registro.html')
