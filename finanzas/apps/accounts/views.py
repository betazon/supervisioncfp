# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect, HttpResponse, render_to_response
from django.template import Context, Template, RequestContext
from django.contrib import auth
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import Group, Permission, User
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.core.mail import EmailMultiAlternatives
from django.core.urlresolvers import reverse
from .forms import LoginForm, ChangePassForm, ResetPassForm



def login_view(request):
    request.session.flush()
    if request.user.is_authenticated():#si el usuario esta autenticado redirecciona a la pagina principal
        return HttpResponseRedirect(reverse('principal'))
    form = LoginForm()#declaramos una variable que reciba los campos del formulario
    mensaje = '' #declaramos una variable con un mensaje vacio
    user = None #declaro la variable user a None
    if request.method == 'POST':#validamos que los datos vengan por Post
        form = LoginForm(request.POST)#le pasamos el request a loginForm
        if form.is_valid(): #verificamos que el formato de los datos sea correcto
            usuario = form.data['user']#asignamos a los datos de usuario a una variable usuario
            password = form.cleaned_data['password']#asignamos a los datos de password a una variable password
            user = authenticate(username = usuario, password = password)#validamos que el usuario y la contraseña sean correctos

            if user.is_authenticated:
                request.session['user'] = usuario
                request.session['password'] = password
                login(request, user)
                return HttpResponseRedirect('principal')
            #elif not request.user.is_authenticated:#el usuario esta logueado, pero esta inactivo es su primer inicio de sesion
            #    request.session['user'] = usuario
            #    request.session['password'] = password
            #    login(request, user)
            #    return HttpResponseRedirect('change_pass')
            else:
                mensaje = 'Usuario y/o password incorrecto, verifíquelo e inténtelo nuevamente.'
        else:
            mensaje = 'Debe completar ambos campos.'#mandamos un mensaje de error
    values = {
        'form' : form,
        'mensaje' : mensaje,
    }
    return render(request, 'login.html', values)

@login_required
def principal_view(request):
    #return redirect(reverse('principal'))
    return render(request, 'principal.html')

@login_required
def change_pass_view(request):
    form = ChangePassForm()
    mensaje = ""
    if request.method == 'POST':
        form = ChangePassForm(request.POST)
        if form.is_valid():
            username = request.user
            password = form.data['password_actual']
            user = authenticate(username=username, password=password)
            if user is not None:
                password_nuevo = form.cleaned_data['password_nuevo']
                password_confirmar = form.cleaned_data['password_confirmar']
                if password_nuevo == password_confirmar:
                    user.set_password(password_nuevo)
                    #if user.is_active == False:
                    #    user.is_active = True
                    try:
                        user.save()
                    except Exception, e:
                        raise e
                    logout(request)
                    return redirect(reverse('login'))
                else:
                    mensaje = "Los password no coinciden."
            else:
                mensaje = "Password actual no coincide con el usuario logueado."
        else:
            mensaje = "Debe completar todos los campos."
    values = {
        'mensaje':mensaje,
        'form':form
        }
    return render(request, 'change_pass.html', values)

@login_required
def logout_view(request):
    logout(request) #cierra sesion
    request.session.flush()
    return redirect(reverse('login'))#redirecciona a login

def reset_pass_view(request):
    form = ResetPassForm()
    mensaje = ""
    query = ""
    if request.method == 'POST':
        form = ResetPassForm(request.POST)
        if form.is_valid():
            email = form.data['email_user']
            query = User.objects.filter(email=email)
            if query:
                user = User.objects.get(email=email)
                random_password = User.objects.make_random_password(length=8)
                user.set_password(random_password)
                #user.is_active = False
                try:
                    user.save()
                    subject = 'Reestablecimiento de password.'
                    html_content = ("Hola:<br>Este correo contiene su usuario y password para acceder al Sistema del Area Finanzas.<br>Recuerde que el password asignado debera cambiarse, al momento de acceder por primera vez al sistema, por uno de su preferencia.<br>Los passwords son personales y confidenciales, por lo tanto Ud. es el unico responsable de las acciones que se ejecuten con el.<br>Sus credenciales son:<br><br>Usuario: %s <br> Password: %s <br>Saludos, equipo de desarrollo."% (user, random_password))
                    from_email = 'Area Finanzas'
                    to = email
                    msg = EmailMultiAlternatives(subject, html_content, from_email, [to])
                    msg.attach_alternative(html_content, "text/html")
                    msg.send()
                except Exception, e:
                    raise e

                return redirect(reverse('login'))
            else:
                mensaje='La dirección de correo electrónico ingresada no es válida.'
        else:
            mensaje = 'Es obligatorio ingresar una dirección de correo electrónico.'
    values = {
        'form':form,
        'mensaje':mensaje,
    }
    return render (request, 'reset_pass.html', values)
