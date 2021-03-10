from django.contrib import admin
from .models import Servicio


class Servicio_Admin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')


admin.site.register(Servicio, Servicio_Admin)
