from django.shortcuts import render
from .models import Producto, CategoriaProd


def tienda(request):

    productos = Producto.objects.all()

    categorias = CategoriaProd.objects.all()

    return render(request, "tienda/tienda.html", {"productos": productos, "categorias": categorias})


def categoria(request, id):

    categorias = CategoriaProd.objects.all()

    categoria_sel = CategoriaProd.objects.get(id=id)

    productos = Producto.objects.filter(categorias=categoria_sel)

    return render(request, "tienda/categoria.html", {'categorias': categorias, 'categoria': categoria_sel,
                                                     'productos': productos })
