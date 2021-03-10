from django.urls import path
from . import views

urlpatterns = [
    path('', views.tienda, name='Tienda'),
    path('categoria/<int:id>/', views.categoria, name="categoriaProd"),
]
