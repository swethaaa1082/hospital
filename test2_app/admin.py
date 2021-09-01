from django.contrib import admin
from .models import *
# Register your models here.
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug':('name',)}
admin.site.register(Department,DepartmentAdmin)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ['name','slug','img','position', 'time']
    list_editable = ['time']
    prepopulated_fields = {'slug':('name',)}
admin.site.register(Doctor,DoctorAdmin)
