from django.shortcuts import redirect, render
from .forms import FormularioContacto
from django.core.mail import EmailMessage


def contacto(request):

    formulario_contacto = FormularioContacto()

    if request.method == "POST":

        formulario_contacto = FormularioContacto(data=request.POST)

        if formulario_contacto.is_valid():

            nombre = request.POST.get("nombre")
            email = request.POST.get("email")
            telefono = request.POST.get("telefono")
            contenido = request.POST.get("contenido")

            email=EmailMessage("Mensaje desde App Django",
            "El usuario: {}, telefono: {}, direccion: {}, comenta: \n\n{}".format(nombre,telefono,email,contenido),
            "",["rocodoko21@gmail.com"], reply_to=[email])

            try:
                email.send()
                return redirect('/contacto/?valid')
           
            except:

                return redirect('/contacto/?invalid')

    return render(request, "contacto/contacto.html", {'miFormulario': formulario_contacto})
