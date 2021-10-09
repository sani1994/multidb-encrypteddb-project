from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.models import User
from core_app.models.measurement import Measurement
from core_app.models.user import ConsoleUser

# Register your models here.
admin.site.register(Measurement)
admin.site.unregister(User)
admin.site.unregister(Group)


class UserAdmin(admin.ModelAdmin):

    def measurement(self, obj):
        return Measurement.objects.filter(user_id=obj.id).last() or None

    readonly_fields = ('measurement',)
    list_display = ['name', 'email', 'street']
    fields = [('name', 'email'), ('street', 'street_2', 'city', 'country'), 'measurement']


admin.site.register(ConsoleUser, UserAdmin)
