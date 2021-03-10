from django.contrib import admin
from django.urls import path
from django.urls.conf import include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('servicios/', include('Servicios.urls')),
    path('blog/', include('Blog.urls')),
    path('contacto/', include('Contacto.urls')),
    path('tienda/', include('Tienda.urls')),
    path('', include('ProyectoWebApp.urls')),
]
