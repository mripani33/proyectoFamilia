from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpRequest,HttpResponse



# Create your views here.
def inicio(request):
    return render(request, "appfamilia/index.html")

def familiares(request):
    return render(request, "appfamilia/familiares.html") 