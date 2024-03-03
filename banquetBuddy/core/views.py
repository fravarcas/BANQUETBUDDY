from django.shortcuts import render, redirect
from .forms import EmailAuthenticationForm
from django.contrib.auth import authenticate, login, logout

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

def logout_view(request):
    logout(request) 
    return redirect('/')

def login_view(request):
    if request.user.is_authenticated:
        return redirect('/')
    elif request.method == 'POST':
        form = EmailAuthenticationForm(request, request.POST)
        
        if form.is_valid():
            email = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('/')
    else:
        form = EmailAuthenticationForm()
    return render(request, 'core/login.html', {'form': form})
