# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Ciudad(models.Model):
    descripcion = models.CharField(max_length = 30)

    class Meta:
        ordering = ['descripcion']
        verbose_name_plural = "Ciudades"

    def __unicode__(self):
        return self.descripcion

class Persona(models.Model):
    apellido = models.CharField(max_length = 30)
    nombre = models.CharField(max_length = 30)
    documento = models.CharField(max_length = 8)
    telefono = models.CharField(max_length = 11)
    email = models. EmailField()
    direccion = models.CharField(max_length = 50)
    ciudad = models.ForeignKey(Ciudad)

    class Meta:
        ordering = ['apellido']
        verbose_name_plural = "Personas"

    def __unicode__(self):
        return '%s %s' %(self.apellido, self.nombre)

class Alumnos(models.Model):
    apellido = models.CharField(max_length = 30)
    nombre = models.CharField(max_length = 30)
    documento = models.CharField(max_length = 8)
    telefono = models.CharField(max_length = 11)
    email = models. EmailField()
    direccion = models.CharField(max_length = 50)
    ciudad = models.ForeignKey(Ciudad)
    fecha_nac = models.DateField()
    lugar_nac = models.CharField(max_length = 30)
     

    class Meta:
        ordering = ['apellido']
        verbose_name_plural = "Alumnos"

    def __unicode__(self):
        return '%s %s' %(self.apellido, self.nombre)

class Docentes (models.Model):

    apellido = models.CharField(max_length = 30)
    nombre = models.CharField(max_length = 30)
    documento = models.CharField(max_length = 8)
    telefono = models.CharField(max_length = 11)
    email = models. EmailField()
    direccion = models.CharField(max_length = 50)
    ciudad = models.ForeignKey(Ciudad)
    fecha_nac = models.DateField()
    lugar_nac = models.CharField(max_length = 30)
    
    

    class Meta:
        ordering = ['apellido']
        verbose_name_plural = "Docentes"

    def __unicode__(self):
        return '%s %s' %(self.apellido, self.nombre)

class Cfp (models.Model):
    cue = models.CharField(max_length = 15)
    nombre = models.CharField(max_length = 30)
    director = models.CharField(max_length = 30)
    domicilio = models.CharField(max_length = 30)
    sede = models.CharField(max_length = 2)
    calificacion = models.CharField(max_length = 2)

    class Meta:
        ordering = ['nombre']
        verbose_name_plural = "Cfps"

    def __unicode__(self):
        return self.nombre


class Cursos (models.Model):
    docente = models.ForeignKey(Docentes)
    fecha_ini = models.CharField(max_length = 8)
    fecha_fin = models.CharField(max_length = 8)
    sede = models.CharField(max_length = 2)
    cfp = models.ForeignKey(Cfp)
    desgranamiento = models.CharField(max_length = 2)
    



class Asistencia (models.Model):
    fecha = models.CharField(max_length = 8)
    alumnos = models.ForeignKey(Alumnos)
    estado = models.CharField(max_length = 8)
    cursos = models.ForeignKey(Cursos)

    class Meta:
        ordering = ['alumnos']
        verbose_name_plural = "Asistencias"

    def __unicode__(self):
        return self.nombre




class clases(models.Model):
    cursos = models.ForeignKey(Cursos)
    alumnos = models.ForeignKey(Alumnos)
    asistencia = models.ForeignKey(Asistencia)
    fecha = models.DateField()    





class Jerarquia(models.Model):
    descripcion = models.CharField(max_length = 30)

    class Meta:
        ordering = ['descripcion']
        verbose_name_plural = "Jerarquias"

    def __unicode__(self):
        return self.descripcion

class Tipo_empleado(models.Model):
    descripcion = models.CharField(max_length = 30)

    class Meta:
        ordering = ['descripcion']
        verbose_name_plural = "Tipos de Empleados"

    def __unicode__(self):
        return self.descripcion

class Seccion(models.Model):
    descripcion = models.CharField(max_length = 30)

    class Meta:
        ordering = ['descripcion']
        verbose_name_plural = "Secciones"

    def __unicode__(self):
        return self.descripcion

class Agrupacion(models.Model):
    descripcion = models.CharField(max_length = 30)

    class Meta:
        ordering = ['descripcion']
        verbose_name_plural = "Agrupaciones"

    def __unicode__(self):
        return self.descripcion

class Escalafon(models.Model):
    descripcion = models.CharField(max_length = 30)
    agrupacion = models.ForeignKey(Agrupacion)

    class Meta:
        ordering = ['descripcion']
        verbose_name_plural = "Escalafones"

    def __unicode__(self):
        return self.descripcion

class Sexo (models.Model):
    descripcion = models.CharField(max_length = 30)

    class Meta:
        ordering = ['descripcion']
        verbose_name_plural = "Sexos"

    def __unicode__(self):
        return self.descripcion

class Empleado(models.Model):
    persona = models.ForeignKey(Persona)
    seccion = models.ForeignKey(Seccion)
    sexo = models.ForeignKey(Sexo)
    tipo_empleado = models.ForeignKey(Tipo_empleado)
    agrupacion = models.ForeignKey(Agrupacion)

    class Meta:
        #ordering = ['descripcion']
        verbose_name_plural = "Empleados"
