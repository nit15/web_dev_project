from django.shortcuts import render
from django import forms
from django.shortcuts import redirect
tasks=[]
# Create your views here.
class Newtaskform(forms.Form):
    task=forms.CharField(label="New task:")
    priority=forms.IntegerField(label="Priority:", min_value=0, max_value=5)

def index(request):
    if "tasks" not in request.session:
        request.session["tasks"]=[]

    return render(request,"tasks/home.html",{
        'tasks':request.session["tasks"]
    })

def add(request):
    if request.method =='POST':
        form=Newtaskform(request.POST)
        if form.is_valid():
            task=form.cleaned_data["task"]
            request.session["tasks"]+=[task]
            return redirect("home")
        else:
         return render(request,"tasks/newtask.html",{
        'Form':Newtaskform() })
    return render(request, "tasks/newtask.html", {
         'Form': Newtaskform()
    })
