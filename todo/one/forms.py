from django import forms
from .models import *
from django.forms import ModelForm


class TaskFrom(forms.ModelForm):
    # tao chu mo trong phan nhap input
    title = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Add new task...'}))
    
    class Meta:
        model = Task
        fields = '__all__'
