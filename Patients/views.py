from django.shortcuts import render, redirect
from .models import Patient
from .forms import PatientForm
from django.http import HttpResponse

def home(request):
    # response_content = "Hello, this is the response content!"

    # return HttpResponse(response_content)
    context = {
        'title':"We Cure"
    }
    return render(request,'Patients/index.html',context)

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
