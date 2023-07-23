from django.shortcuts import render, redirect
from .models import Patient
from .forms import PatientForm
from django.http import HttpResponse

def all_patients(request):
    response_content = "Hello, this is the response content!"
    return HttpResponse(response_content)

def patient_form(request):
    if request.method == 'POST':
        form = PatientForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            # return redirect()

    else:
        form = PatientForm()

    context = {
        'title':'New Patient Form',
        # 'form':form
    }
    return render(request,'Patients/patient_form.html',context)
