# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Ciudad, Persona, Jerarquia, Tipo_empleado, Seccion, Agrupacion, Escalafon, Sexo, Empleado, Cfp

admin.site.register(Ciudad)
admin.site.register(Persona)
admin.site.register(Jerarquia)
admin.site.register(Tipo_empleado)
admin.site.register(Seccion)
admin.site.register(Agrupacion)
admin.site.register(Escalafon)
admin.site.register(Sexo)
admin.site.register(Empleado)
admin.site.register(Cfp)

