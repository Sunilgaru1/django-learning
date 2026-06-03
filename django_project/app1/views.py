from django.shortcuts import render
from .models import AppVarity
from django.shortcuts import get_object_or_404

# Create your views here.
def all_apps(request):
    apps = AppVarity.objects.all()
    return render(request , 'app1/all_app1.html',{'apps' : apps})

def app_detail(request,app_id):
    app = get_object_or_404(AppVarity , pk=app_id)
    return render(request ,'app1/app_details.html', {'app':app})