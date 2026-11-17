from django.contrib import admin

from .models import Activity, Club

admin.site.register(Club)
admin.site.register(Activity)