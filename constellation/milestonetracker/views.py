from django.shortcuts import render
from .models import dops

def home(request):
    return render(request, 'milestonetracker/home.html', {})

def all_dops(request):
    all_dops = dops.objects.all()

    return render(request, 'milestonetracker/dops.html', 
        {'all_dops': all_dops})