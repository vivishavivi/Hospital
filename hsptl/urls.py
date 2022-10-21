from django.urls import path
from . import views
urlpatterns=[
    path('',views.index,name='index'),
    path('doctors',views.doctors,name='doctors'),
    path('department',views.department,name='department'),
    path('booking',views.booking,name='booking'),
    path('about',views.about,name='about'),
    path('contact',views.contact,name='contact'),
]