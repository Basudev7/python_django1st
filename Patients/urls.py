from django.urls import path
from .views import *

app_name = "Patients"

urlpatterns = [
    path('patient_form',patient_form,name="patient_form"),
    path('',all_patients, name="all")
]