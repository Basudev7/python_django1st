from django.contrib import admin
from .models import Patient

class PatientAdmin(admin.ModelAdmin):
    model = Patient
    list_display = ('name','email','phone_number','country','stage')
    list_filter = ['status','stage']
    search_fields = ['name']

admin.site.register(Patient,PatientAdmin)
