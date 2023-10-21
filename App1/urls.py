from django.urls import path
from App1 import views

urlpatterns = [
                path('informacion/', views.informacion, name="Informacion"),

                path('catalogo/list/', views.CatalogoList.as_view(), name='CatalogoList'),
                path('catalogo/detalle/<int:pk>', views.CatalogoDetalle.as_view(), name='CatalogoDetail'),
                path('catalogo/nuevo/', views.CatalogoCreacion.as_view(), name='CatalogoNew'),
                path('catalogo/edit/<int:pk>', views.CatalogoUpdate.as_view(), name='CatalogoEdit'),
                path('catalogo/eliminar/<int:pk>', views.CatalogoDelete.as_view(), name='CatalogoDelete'),
                
                path('cliente/list/', views.ClienteList.as_view(), name='ClienteList'),
                path('cliente/detalle/<int:pk>', views.ClienteDetalle.as_view(), name='ClienteDetail'),
                path('cliente/nuevo/', views.ClienteCreacion.as_view(), name='ClienteNew'),
                path('cliente/edit/<int:pk>', views.ClienteUpdate.as_view(), name='ClienteEdit'),
                path('cliente/eliminar/<int:pk>', views.ClienteDelete.as_view(), name='ClienteDelete'),
                
                path('proveedor/list/', views.ProveedorList.as_view(), name='ProveedorList'),
                path('proveedor/detalle/<int:pk>', views.ProveedorDetalle.as_view(), name='ProveedorDetail'),
                path('proveedor/nuevo/', views.ProveedorCreacion.as_view(), name='ProveedorNew'),
                path('proveedor/edit/<int:pk>', views.ProveedorUpdate.as_view(), name='ProveedorEdit'),
                path('proveedor/eliminar/<int:pk>', views.ProveedorDelete.as_view(), name='ProveedorDelete'),
]
