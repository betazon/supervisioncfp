# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.shortcuts import render, redirect
from finanzas.apps.personal.forms import *
from .models import *

def cfp_create_view(request):
    form = CfpForm()
    mensaje =""
        
    if request.method == 'POST':
        form = CfpForm(request.POST)
        print(form.errors)
        if form.is_valid():
            cfp = CfpForm()
           
            cue = form.cleaned_data['cue']
            nombre = form.cleaned_data['nombre']
            director = form.cleaned_data['director']
            domicilio = form.cleaned_data['domicilio']
            calificacion = form.cleaned_data ['calificacion']
            
            form.cue = cue
            form.nombre = nombre
            form.director = director
            form.domicilio = domicilio
            form.save()
           
            return redirect('cfp')
        else:
            mensaje = "Los datos no son validos :P"
    
    values = {'form':form, 'mensaje':mensaje}
    return render(request, "formulario_cfp.html", values)



def personal_create_view(request):
    form = PersonaForm()
    mensaje= ""
   
    if request.method == 'POST':
        form = PersonaForm(request.POST)
        print(form.errors)
        if form.is_valid():
            personales = PersonaForm()
                       
            apellido = form.cleaned_data['apellido']
            nombre = form.cleaned_data['nombre']
            documento = form.cleaned_data['documento']
            telefono = form.cleaned_data['telefono']
            email = form.cleaned_data ['email']
            direccion = form.cleaned_data['direccion']
            ciudad = form.cleaned_data['ciudad']
           
            form.apellido = apellido
            form.nombre = nombre
            form.documento = documento
            form.telefono = telefono
            form.email = email
            form.direccion = direccion
            form.ciudad_id = ciudad.id
            form.save()

            return redirect('listar')

            mensaje = "Datos Grabados con exitos"
        else:
            mensaje = "Los datos no son validos :P"
    values = {
        'form':form,
        'mensaje':mensaje,
                     }
    return render(request, 'formulario_empleado.html', values)


def alumnos_create_view(request):
    form = PersonaForm()
    mensaje= ""
   
    if request.method == 'POST':
        form = PersonaForm(request.POST)
        print(form.errors)
        if form.is_valid():
            personales = PersonaForm()
                       
            apellido = form.cleaned_data['apellido']
            nombre = form.cleaned_data['nombre']
            documento = form.cleaned_data['documento']
            telefono = form.cleaned_data['telefono']
            email = form.cleaned_data ['email']
            direccion = form.cleaned_data['direccion']
            ciudad = form.cleaned_data['ciudad']
           

            form.apellido = apellido
            form.nombre = nombre
            form.documento = documento
            form.telefono = telefono
            form.email = email
            form.direccion = direccion
            form.ciudad_id = ciudad.id
            form.save()

            return redirect('listar')

            mensaje = "Datos Grabados con exitos"
        else:
            mensaje = "Los datos no son validos :P"
    values = {
        'form':form,
        'mensaje':mensaje,
                     }
    return render(request, 'formulario_empleado.html', values)




def cfp_delete_view(request, cfp_id):

    borracfp = Cfp.objects.get(id=cfp_id)
    form = CfpForm(instance=borracfp)
    borracfp.delete()
    lista_cfp = Cfp.objects.all()
    values = {
        'lista_cfp':lista_cfp,
    }
    return render(request, 'lista_cfp.html', values)

def alumnos_delete_view(request, alumnos_id):

    borraalumnos = Alumnos.objects.get(id=alumnos_id)
    form = alumnosForm(instance=borracfp)
    borraalumnos.delete()
    lista_alumnos = alumnos.objects.all()
    values = {
        'lista_alumnos':lista_cfp,
    }
    return render(request, 'lista_alumnos.html', values)

    

    
    
def cfp_list_view(request):
    lista_cfp = Cfp.objects.all()
    values = {
        'lista_cfp':lista_cfp,
    }
    return render(request, 'lista_cfp.html', values)


def personal_list_view(request):
    lista = Persona.objects.all()
    values = {
        'lista':lista,
    }
    return render(request, 'lista_empleado.html', values)


def alumnos_list_view(request):
    lista_alumnos = Alumnos.objects.all()
    values = {
        'lista_alumnos':lista_alumnos,
    }
    return render(request, 'lista_alumnos.html', values)





def cfp_update_view(request,cfp_id):

    numerodecfp = Cfp.objects.get(pk=cfp_id)
    form = CfpForm(instance=numerodecfp)
    
    mensaje = ""
    if request.method == 'POST':
        form = CfpForm(request.POST, instance=numerodecfp)

        if form.is_valid():
            
            cfp = CfpForm()
            cue = form.cleaned_data['cue']
            nombre = form.cleaned_data['nombre']
            director = form.cleaned_data['director']
            domicilio = form.cleaned_data['domicilio']
            calificacion = form.cleaned_data ['calificacion']
            
            cfp.cue = cue
            cfp.nombre = nombre
            cfp.director = director
            cfp.domicilio = domicilio
            cfp.calificacion = calificacion
   
            form.save()
            mensaje = "Los datos de la escuela Fueron Modificados"
        else:
            mensaje = "Los datos no son validos :P"
    
    values = {'form':form, 'mensaje':mensaje}
    return render(request, 'editar_cfp.html', values)





def personal_update_view(request,persona_id):

    documentopersona=Persona.objects.get(pk=persona_id)
    form = PersonaForm(instance=documentopersona)

    mensaje = ""
    if request.method == 'POST':
        form = PersonaForm(request.POST, instance=documentopersona)

        if form.is_valid():

            personales = Persona()
            apellido = form.cleaned_data['apellido']
            nombre = form.cleaned_data['nombre']
            documento = form.cleaned_data['documento']
            telefono = form.cleaned_data['telefono']
            email = form.cleaned_data['email']
            direccion = form.cleaned_data['direccion']
            ciudad = form.cleaned_data['ciudad']
            

            personales.apellido = apellido
            personales.nombre = nombre
            personales.documento = documento
            personales.telefono = telefono
            personales.email = email
            personales.direccion = direccion
            personales.ciudad_id = ciudad.id
            form.save()

            mensaje = "Los datos de la persona fueron Modificados"
        else:
            mensaje = "Los datos no son validos"
    values = {'form': form,  'mensaje': mensaje}
    return render(request, 'editar_empleado.html', values)

def alumnos_update_view(request,persona_id):

    documentopersona=Persona.objects.get(pk=persona_id)
    form = PersonaForm(instance=documentopersona)

    mensaje = ""
    if request.method == 'POST':
        form = PersonaForm(request.POST, instance=documentopersona)

        if form.is_valid():

            personales = Persona()
            apellido = form.cleaned_data['apellido']
            nombre = form.cleaned_data['nombre']
            documento = form.cleaned_data['documento']
            telefono = form.cleaned_data['telefono']
            email = form.cleaned_data['email']
            direccion = form.cleaned_data['direccion']
            ciudad = form.cleaned_data['ciudad']
            

            personales.apellido = apellido
            personales.nombre = nombre
            personales.documento = documento
            personales.telefono = telefono
            personales.email = email
            personales.direccion = direccion
            personales.ciudad_id = ciudad.id
            form.save()

            mensaje = "Los datos de la persona fueron Modificados"
        else:
            mensaje = "Los datos no son validos"
    values = {'form': form,  'mensaje': mensaje}
    return render(request, 'editar_empleado.html', values)

def personal_delete_view(request, persona_id):
    

    borrapersona = Persona.objects.get(id=persona_id)
    form = PersonaForm(instance=borrapersona)
    borrapersona.delete()
    lista = Persona.objects.all()

    values = {'lista':lista, }

    return render(request, 'lista_empleado.html', values)


 
def personal_cargartxt_view(request):

    infile = open('liqpoli.txt', 'r')
    
    print('>>> Lectura del fichero línea a línea')
    for line in infile:
        print(line)
    infile.close()

    return render(request, 'cargar_txt.html')

