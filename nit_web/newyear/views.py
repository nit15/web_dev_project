from django.shortcuts import render
from datetime import datetime
# Create your views here.
def index(request):
    now=datetime.now()
    return render(request,"newyear\home.html",{
        'newyear':now.day==7 and now.month==11
    })
