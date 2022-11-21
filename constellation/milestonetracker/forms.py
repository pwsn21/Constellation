from django import forms
from django.forms import ModelForm
from .models import dops

class dopsform(ModelForm):
    class Meta:
        model = dops
        fields = ('dops_date', 'mentor', 'msnumber', 'comments',)

        labels = {
            'dops_date': '',
            'mentor': '',
            'msnumber': '',
            'comments': '',
        }

        widgets = {
            'dops_date': forms.DateTimeInput(attrs={'class':'form-control', 'placeholder':'Date'}),
            'mentor': forms.Select(attrs={'class':'form-control', 'placeholder':'Mentor'}),
            'msnumber': forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Milestone Number'}),
            'comments': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Comments'})
        }