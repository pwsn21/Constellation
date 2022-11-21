from django.shortcuts import render
from .models import dops
from .forms import dopsform
from django.http import HttpResponseRedirect

def home(request):
    return render(request, 'milestonetracker/home.html', {})

def dopsview(request):
    dopsview = dops.objects.all()

    return render(request, 'milestonetracker/dopsview.html', 
        {'dopsview': dopsview})

def dopsadd(request):
    submitted = False
    if request.method =="POST":
        form = dopsform(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/dopsadd?submitted=True')
    else:
        form = dopsform
        if 'submitted' in request.GET:
            submitted = True
    
    return render(request, 'milestonetracker/dopsadd.html', 
        {'form': form, 'submitted':submitted})