from django.urls import path
from . import views

#localhost:8000/apps

urlpatterns = [
    path('',views.all_apps,name= 'all_apps'),
    path('<int:app_id>/',views.app_detail,name= 'app_detail'),
]
