from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
  return HttpResponse("Hello world..!")

def greetings(request,name):
  #return HttpResponse(f"Hello {name.upper()}")
  return render(request,"hello\home.html",{
    'name':name
  })

