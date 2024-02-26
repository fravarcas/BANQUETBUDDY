from django.shortcuts import render

def home(request):
    return render(request, 'core/home.html')

def about_us(request):
    return render(request, 'core/aboutus.html')

def faq(request):
    return render(request, 'core/faq.html')
    
def contact(request):
    return render(request, 'core/contact.html')
