from django.http import HttpResponse
from django.shortcuts import render


def home(request):

    #return HttpResponse("Hello User , You are now at Home Page.")
    return render(request,'website/home/index.html')

def about(request):
    # return HttpResponse("Hello User , You are now at About Page.")
    return render(request,'website/about/indexforabout.html')

def contact(request):
    # return HttpResponse("Hello User , You are now at Contact Page.")
    return render(request,'website/contact/index.html')