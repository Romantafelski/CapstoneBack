from django.contrib import admin

# Register your models here.

from .models import Tattoo
from .models import Admin
admin.site.register(Tattoo)
admin.siteregister(Admin)
