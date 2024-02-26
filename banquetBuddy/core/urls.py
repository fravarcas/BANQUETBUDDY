from django.urls import path
from . import views
from django.urls import path, include
from core.views import *

urlpatterns = [
    path('', home, name='home'),
    path('about-us', about_us, name='about_us'),
    path('subscription-plans', about_us, name='subscription_plans')
    path('preguntas-rapidas', faq, name='faq')

]
