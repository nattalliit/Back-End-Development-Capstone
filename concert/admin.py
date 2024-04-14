from django.contrib import admin

# Register your models here.
from .models import Concert

#Register the Concert model with the admin interface
admin.site.register(Concert)
