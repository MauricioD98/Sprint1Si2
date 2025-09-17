# visualizacion_expedientes/urls.py
from django.urls import path
from . import views

urlpatterns = [
    # URLs para TipoDocumento
    path('tipos_documento/', views.tipo_documento_list, name='tipo_documento_list'),
    path('tipos_documento/nuevo/', views.tipo_documento_create, name='tipo_documento_create'),
    path('tipos_documento/<int:pk>/editar/', views.tipo_documento_update, name='tipo_documento_update'),
    path('tipos_documento/<int:pk>/eliminar/', views.tipo_documento_delete, name='tipo_documento_delete'),

    # URLs para Documento
    path('documentos/', views.documento_list, name='documento_list'),
    path('documentos/nuevo/', views.documento_create, name='documento_create'),
    path('documentos/<int:pk>/editar/', views.documento_update, name='documento_update'),
    path('documentos/<int:pk>/eliminar/', views.documento_delete, name='documento_delete'),

    # URLs para Tiene
    path('relaciones_caso_cliente/', views.tiene_list, name='tiene_list'),
    path('relaciones_caso_cliente/nueva/', views.tiene_create, name='tiene_create'),
    path('relaciones_caso_cliente/<int:pk>/editar/', views.tiene_update, name='tiene_update'),
    path('relaciones_caso_cliente/<int:pk>/eliminar/', views.tiene_delete, name='tiene_delete'),
    
    # URL para la vista jerárquica de expedientes
    path('jerarquia/', views.expedientes_jerarquicos, name='expedientes_jerarquicos'), # <--- Añade esta línea
]