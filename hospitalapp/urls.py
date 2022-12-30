from django.urls import path
from hospitalapp import views

urlpatterns=[
    path('',views.home,name='home'),
path('about',views.about,name='about'),
path('booking',views.booking,name='booking'),
path('doctors',views.doctors,name='doctors'),
path('department',views.department,name='department'),
path('contact',views.contact,name='contact'),
path('signup',views.signup,name='signup'),
]