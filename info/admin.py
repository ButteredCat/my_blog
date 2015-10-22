from django.contrib import admin

from solo.admin import SingletonModelAdmin
from .models import Info

# Register your models here.
admin.site.register(Info, SingletonModelAdmin)

config = Info.get_solo()

