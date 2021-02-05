import datetime

from django import forms
from django.core import validators

   
class ContactForm(forms.Form):
    nombre = forms.CharField(max_length=100,required=True)
    apellido = forms.CharField (max_length=100)
    email = forms.EmailField()
    mensaje = forms.CharField(widget=forms.Textarea)
  