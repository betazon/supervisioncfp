from django.conf.urls import include, url
from .views import(personal_create_view, personal_list_view, 
	personal_update_view, personal_delete_view, personal_cargartxt_view,
	cfp_list_view,cfp_create_view, cfp_delete_view, cfp_update_view,
	alumnos_list_view,alumnos_create_view,alumnos_delete_view,alumnos_update_view)

urlpatterns = [
    url(r'^crear/$', personal_create_view, name='crear'),
    url(r'^listar/$', personal_list_view, name='listar'),
    url(r'^editar/(?P<persona_id>[0-9]+)/', personal_update_view, name='editar'),
    url(r'^borrar/(?P<persona_id>[0-9]+)/', personal_delete_view, name='borrar'),
    url(r'^cargar_txt/$', personal_cargartxt_view, name='cargar_txt'),
    url(r'^cfp/$', cfp_list_view, name='cfp'),
    url(r'^crear_cfp/$', cfp_create_view, name='crear_cfp'),
    url(r'^borrar_cfp/(?P<cfp_id>[0-9]+)/', cfp_delete_view, name='borrar_cfp'),
    url(r'^editar_cfp/(?P<cfp_id>[0-9]+)/', cfp_update_view, name='editar_cfp'),
 	url(r'^alumnos/$', alumnos_list_view, name='alumnos'),
    url(r'^crear_alumnos/$', alumnos_create_view, name='crear_alumnos'),
    url(r'^borrar_alumnos/(?P<cfp_id>[0-9]+)/', alumnos_delete_view, name='borrar_cfp'),
    url(r'^editar_alumnos/(?P<cfp_id>[0-9]+)/', alumnos_update_view, name='editar_cfp'),
       
]
