from django.conf.urls import url
from apps.mascota.views import index,listadousuarios,mascota_view,mascota_list,mascota_edit,mascota_delete,MascotaList,MascotaCreate,MascotaUpdate,MascotaDelete
from django.contrib.auth.decorators import login_required

urlpatterns = [
    url(r'^$', index,name='index'),
    # url(r'^nuevo$', mascota_view, name='mascota_crear'), #Vista basada en Funciones
    url(r'^nuevo$', login_required(MascotaCreate.as_view()), name='mascota_crear'), #Vista basada en Clases
    # url(r'^listar', mascota_list, name='mascota_listar'), #Vista Basada en Funciones
    url(r'^listar', login_required(MascotaList.as_view()), name='mascota_listar'), #Vista basada en clases
    #url(r'^editar/(?P<id_mascota>\d+)/$', mascota_edit, name='mascota_editar'),
    url(r'^editar/(?P<pk>\d+)/$', login_required(MascotaUpdate.as_view()), name='mascota_editar'),
    #url(r'^eliminar/(?P<id_mascota>\d+)/$', mascota_delete, name='mascota_eliminar'),
    url(r'^eliminar/(?P<pk>\d+)/$', login_required(MascotaDelete.as_view()), name='mascota_eliminar'),

    url(r'^listado', listadousuarios, name="listado"),
]
