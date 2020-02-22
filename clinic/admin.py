from django.contrib import admin
from .models import Patient
from django.db import models
from django.forms import TextInput, Textarea
from django.contrib.auth.models import User
from django.contrib.auth.models import Group

# Register your models here.
admin.AdminSite.site_header = 'Dr. Tarik Assi Clinic'
admin.AdminSite.site_title = 'Patients Adminstration'
admin.AdminSite.index_title = 'Patients Adminstration'
admin.site.unregister(User)
admin.site.unregister(Group)


class PatientAdmin(admin.ModelAdmin):
    list_display = ('get_full_name', 'date_of_birth')
    fieldsets = [
        ('Personal Information', {'fields': ['first_name', 'last_name', 'date_of_birth', 'height', 'weight']}),
        ('Medical Informaion', {'fields': ['history', 'physical_examination']})
    ]

    search_fields = ['first_name', 'last_name']

    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size': 20})},
        models.TextField: {'widget': Textarea(attrs={'rows': 4, 'cols': 40})},
    }


admin.site.register(Patient, PatientAdmin)
