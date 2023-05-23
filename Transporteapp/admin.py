from django import forms
from django.contrib import admin
from django.contrib.auth.models import Group, User
from Transporteapp.models import Cliente, Cotización, Vehículo, Bitacora
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static



class TransportistasSelect(forms.Select):
    def get_queryset(self):
        return User.objects.filter(groups__name='Transportistas').exclude(is_superuser=True)
    
    def build_attrs(self, *args, **kwargs):
        attrs = super().build_attrs(*args, **kwargs)
        attrs.update({'class': 'select2'})
        return attrs


class BitacoraAdminForm(forms.ModelForm):
    class Meta:
        model = Bitacora
        fields = '__all__'
        widgets = {
            'transportistas': TransportistasSelect()
        }

class BitacoraAdmin(admin.ModelAdmin):
    form = BitacoraAdminForm
    list_display = ('cliente', 'fecha', 'numeroSeguimiento', 'comentario', 'valor', 'display_transportistas')

    def display_transportistas(self, obj):
        return ", ".join([transportista.username for transportista in obj.transportistas.all()])
    


class GroupAdmin(admin.ModelAdmin):
    list_display = ('name', 'empleados')

    def empleados(self, obj):
        empleados = obj.user_set.all()
        return ", ".join([user.username for user in empleados])



admin.site.unregister(Group)
admin.site.register(Group, GroupAdmin)
admin.site.register(Bitacora, BitacoraAdmin)
admin.site.register(Vehículo)
admin.site.register(Cliente)
admin.site.register(Cotización)