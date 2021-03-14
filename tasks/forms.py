from django import forms
from django.forms import ModelForm

from .models import *

class taskAdd(forms.ModelForm):
    """docstring for ."""
    class Meta:
        model = Task
        fields = '__all__'
