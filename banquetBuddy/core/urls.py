from django.urls import path
from . import views
from django.urls import path, include
from core.views import *

urlpatterns = [
    path('', home, name='home'),
    path('about-us', about_us, name='about_us'),
    path('contact', contact, name='contact'),
    path('subscription-plans', subscription_plans, name='subscription_plans'),
    path('faq', faq, name='faq'),
    path('register_particular',register_particular,name='register_particular'),
    path('register_employee',register_employee,name='register_employee'),
    path('register_company',register_company,name='register_company'),
    path('register_choice', elegir_registro, name='register_choice')

]
