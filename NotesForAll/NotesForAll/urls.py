
from django.contrib import admin
from django.urls import path
from mainApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.upload_notes),
    path('done/', views.upload_complete, name='done'),
    path('twilio', views.inbound_sms, name='sms'),
    
    # path('sms/', 'django_twilio.views.message',{
    #      'message': 'message is here now!'
    # }),
    
    path('search/', views.search, name='search'),
]
