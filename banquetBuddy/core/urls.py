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
    path('logout/', logout_view, name='logout'),
    path('login', login_view, name='login')
]
