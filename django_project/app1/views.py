from django.shortcuts import render
from .models import appVarity
# Create your views here.
def all_app1(request):
    Apps = appVarity.objects.all()
    return render(request , 'app1/all_app1.html',{'Apps' : Apps})
