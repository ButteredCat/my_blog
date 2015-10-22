from django.contrib import admin

from solo.admin import SingletonModelAdmin
from .models import Info

# Register your models here.
class InfoAdmin(SingletonModelAdmin):
    pass

admin.site.register(Info, InfoAdmin)

