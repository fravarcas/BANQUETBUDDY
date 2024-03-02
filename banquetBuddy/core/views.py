from django.shortcuts import redirect, render

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
    #return render(request, 'core/home.html')
    return redirect('/')