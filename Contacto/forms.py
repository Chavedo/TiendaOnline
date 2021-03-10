from django import forms



class FormularioContacto(forms.Form):

    nombre = forms.CharField(label='Nombre', required=True, max_length=50)

    email = forms.EmailField(label='Email', required=True, max_length=60)

    telefono= forms.IntegerField(label='Telefono',required=False, max_value=1000000000000)

    contenido = forms.CharField(
        label='Contenido', max_length=200, widget=forms.Textarea, required=True)
