from django.shortcuts import render

def home(request):
    return render(request, 'core/home.html')

def about_us(request):
    return render(request, 'core/aboutus.html')

def subscription_plans(request):
    return render(request, 'core/subscriptionsplans.html')