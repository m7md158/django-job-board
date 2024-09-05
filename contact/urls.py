from django.urls import path , include
from . import views

app_name = 'contact'  # name of the app

urlpatterns =[
    path('',views.send_message, name= 'contact'),

]