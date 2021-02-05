import json
import time

from django.shortcuts import render , redirect
import requests
from .forms import ContactForm
from django.conf import settings
from django.contrib import messages

# Create your views here.

def inicio(request):
    valores = []
    response = requests.get('https://rickandmortyapi.com/api/character')
    todos = response.json()
    valores.append(todos['results'])


    if request.method == 'GET':
        formulario = ContactForm()
        valores.append(formulario)

    elif request.method == 'POST':
        formulario_devuelto = ContactForm(request.POST)
        if formulario_devuelto.is_valid() == True:
            datos_formulario = formulario_devuelto.cleaned_data
            print(datos_formulario)
            filename = "/app/data/contacto.json"
            with open(str(settings.BASE_DIR)+filename,'r') as file:
                contactos = json.load(file)
                contactos['contactos'].append(datos_formulario)
            with open(str(settings.BASE_DIR)+filename,'w') as file:
                json.dump(contactos,file)
            formulario = ContactForm()
            valores.append(formulario)
            context = {'lista_contactos':contactos['contactos']}
            valores.append(context)
            messages.success(request, 'Mensaje enviado')
            #return redirect('app:inicio')
        else:
            valores.append(formulario_devuelto)
    
    return render(request, 'app/principal.html', {"todos": valores})
    
