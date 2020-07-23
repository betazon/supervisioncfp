# -*- encoding: utf-8 -*-
from django import forms
from models import *



class CfpForm(forms.ModelForm):
    cue = forms.CharField(widget=forms.TextInput(attrs=dict({'class':'form-control input-block-level', 'placeholder':'Cue'},render_value=False)))
    nombre = forms.CharField(widget=forms.TextInput(attrs=dict({'class': 'form-control input-block-level', 'placeholder': 'Nombre'}, render_value=False)))
    director = forms.CharField(widget=forms.TextInput(attrs=dict({'class':'form-control input-block-level', 'placeholder':'Director'},render_value=False)))
    domicilio = forms.CharField(widget=forms.TextInput(attrs=dict({'class':'form-control input-block-level', 'placeholder':'Domicilio'},render_value=False)))
    sede = forms.CharField(widget=forms.TextInput(attrs=dict({'class':'form-control input-block-level', 'placeholder':'Sede'},render_value=False)))
    calificacion = forms.CharField(widget=forms.TextInput(attrs=dict({'class':'form-control input-block-level','placeholder':'calificacion'},render_value=False)))
    
    class Meta:
        model = Cfp
        exclude = []


class PersonaForm(forms.ModelForm):
    apellido = forms.CharField(widget=forms.TextInput(attrs=dict({'class': 'form-control input-block-level', 'placeholder': 'Apellido'}, render_value=False)))
    nombre = forms.CharField(widget=forms.TextInput(attrs=dict({'class':'form-control input-block-level', 'placeholder':'Nombre'},render_value=False)))
    documento = forms.CharField(widget=forms.TextInput(attrs=dict({'class':'form-control input-block-level', 'placeholder':'Documento'},render_value=False)))
    direccion = forms.CharField(widget=forms.TextInput(attrs=dict({'class':'form-control input-block-level', 'placeholder':'Domicilio'},render_value=False)))
    ciudad = forms.ModelChoiceField(widget=forms.Select(attrs=dict({'class':'form-control input-block-level'})), queryset= Ciudad.objects.all())
    email = forms.CharField(widget=forms.EmailInput(attrs=dict({'class':'form-control input-block-level', 'placeholder':'em@il'},render_value=False)))
    telefono = forms.CharField(widget=forms.TextInput(attrs=dict({'class':'form-control input-block-level', 'placeholder':'Nro. de telefono'},render_value=False)))
    
    class Meta:
        model = Persona
        exclude = []

class AlumnosForm(forms.ModelForm):
    apellido = forms.CharField(widget=forms.TextInput(attrs=dict({'class': 'form-control input-block-level', 'placeholder': 'Apellido'}, render_value=False)))
    nombre = forms.CharField(widget=forms.TextInput(attrs=dict({'class':'form-control input-block-level', 'placeholder':'Nombre'},render_value=False)))
    documento = forms.CharField(widget=forms.TextInput(attrs=dict({'class':'form-control input-block-level', 'placeholder':'Documento'},render_value=False)))
    direccion = forms.CharField(widget=forms.TextInput(attrs=dict({'class':'form-control input-block-level', 'placeholder':'Domicilio'},render_value=False)))
    ciudad = forms.ModelChoiceField(widget=forms.Select(attrs=dict({'class':'form-control input-block-level'})), queryset= Ciudad.objects.all())
    email = forms.CharField(widget=forms.EmailInput(attrs=dict({'class':'form-control input-block-level', 'placeholder':'em@il'},render_value=False)))
    telefono = forms.CharField(widget=forms.TextInput(attrs=dict({'class':'form-control input-block-level', 'placeholder':'Nro. de telefono'},render_value=False)))
    
    class Meta:
        model = Persona
        exclude = []








class EmpleadoForm (forms.ModelForm):

    sexo = forms.ModelChoiceField(widget=forms.Select(attrs=dict({'class':'form-control input-block-level'})), queryset= Sexo.objects.all())
    tipo_empleado = forms.ModelChoiceField(widget=forms.Select(attrs=dict({'class':'form-control input-block-level'})), queryset= Tipo_empleado.objects.all())
    agrupacion = forms.ModelChoiceField(widget=forms.Select(attrs=dict({'class':'form-control input-block-level'})), queryset= Agrupacion.objects.all())
    escalafon = forms.ModelChoiceField(widget=forms.Select(attrs=dict({'class':'form-control input-block-level'})), queryset= Escalafon.objects.all())
    seccion = forms.ModelChoiceField(widget=forms.Select(attrs=dict({'class':'form-control input-block-level'})), queryset= Seccion.objects.all())

    class Meta:
        model = Empleado   
        exclude = []         












        