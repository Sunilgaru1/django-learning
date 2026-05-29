from django.urls import path
from . import views

#localhost:8000/app1

urlpatterns = [
    path('',views.all_app1,name= 'all_app1'),
   
]
