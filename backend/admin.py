from django.contrib import admin
from .models import CameraData
from import_export.admin import ImportExportModelAdmin

# Register your models here.
admin.site.register(CameraData, ImportExportModelAdmin)
