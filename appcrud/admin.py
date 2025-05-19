from django.contrib import admin

# Register your models here.
from.models import user , Todo
admin.site.register(user)
admin.site.register(Todo)