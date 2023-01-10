from django.shortcuts import render, redirect, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import *
from account.models import *
from .forms import *
from django.db.models import F
import sweetify
from account.forms import *
from main.decorators import *
import datetime


def landingpage(request):
    return render(request, 'landingpage/landingpage.html')  

@login_required(login_url='login')
@verified_or_superuser
def profile(request, pk):
    profile = Account.objects.get(id=pk)
    form = RegistrationForm(instance=profile)
    context = {
        'title': 'Profile',
        'profile': profile,
        'form': form,
    }
    return render(request, 'main/profile.html', context)


@user_passes_test(lambda u: u.is_superuser)
def dashboard(request):
    patient_count = Patient.objects.all().count()
    doctor_count = Doctor.objects.all().count()
    staff_count = Staff.objects.all().count()
    appointment_count = Appointment.objects.all().count()
    appointments = Appointment.objects.all()
    context = {
        'title': 'Dashboard',
        'patient_count': patient_count,
        'doctor_count': doctor_count,
        'staff_count': staff_count,
        'appointment_count': appointment_count,
        'appointments': appointments

    }
    return render(request, 'main/dashboard.html', context)

@login_required(login_url='login')
@verified_or_superuser
def patients(request):
    form = PatientForm()
    if request.method == 'POST':
        form = PatientForm(request.POST)
        if form.is_valid():
            form.save()
            sweetify.toast(request, 'Patient added', icon='success')
            return HttpResponseRedirect(reverse('patients'))
        else:
            sweetify.toast(request, 'Invalid details', icon='error')
            return HttpResponseRedirect(reverse('patients'))

            
    context = {
        'title': 'Patients',
        'patients' : Patient.objects.all(),
        'form': form
    }
    return render(request, 'main/patients.html', context)


@login_required(login_url='login')
@verified_or_superuser
def patient_update(request, pk):
    patient = Patient.objects.get(id=pk)
    form = PatientForm_Doctor(instance=patient)
    if request.method == "POST":
        form = PatientForm_Doctor(request.POST, instance=patient)
        if form.is_valid():
            form.save()
            sweetify.toast(request, 'Patient updated', icon='success')
            return HttpResponseRedirect(reverse('patients'))
    context = {
        'title': 'Patient Update',
        'form': form,
        'patient': patient
    }
    return render(request, 'main/patientupdate.html', context)


@login_required(login_url='login')
@verified_or_superuser
def patient_delete(request, pk):
    patient = Patient.objects.get(id=pk)
    if request.method == "POST":
        patient.delete()
        sweetify.toast(request, 'Patient deleted', icon='success')
        return HttpResponseRedirect(reverse('patients'))
    context = {
        'title': 'Patient Delete',
        'patient': patient
    }
    return render(request, 'main/patientdelete.html', context)

@login_required(login_url='login')
@verified_or_superuser
def doctors(request):
    form = DoctorForm()
    if request.method == 'POST':
        form = DoctorForm(request.POST)
        if form.is_valid():
            form.save()
            sweetify.toast(request, 'Doctor added', icon='success')
            return HttpResponseRedirect(reverse('doctors'))
    context = {
        'title': 'Doctors',
        'doctors' : Doctor.objects.all(),
        'form': form
    }
    return render(request, 'main/doctors.html', context)


@login_required(login_url='login')
def doctor_schedule(request):
    context = {
        'title': 'Doctor Schedules',
        'doctors' : Doctor.objects.all(),
    }
    return render(request, 'main/doctorschedule.html', context)


@user_passes_test(lambda u: u.is_superuser)
def doctor_update(request, pk):
    doctor = Doctor.objects.get(id=pk)
    form = DoctorForm(instance=doctor)
    if request.method == 'POST':
        form = DoctorForm(request.POST, instance=doctor)
        if form.is_valid():
            form.save()
            sweetify.toast(request, 'Doctor updated successfully', icon='success')
            return HttpResponseRedirect(reverse('doctors'))
    context = {
        'title': 'Doctor Update',
        'form': form
    }
    return render(request, 'main/doctorupdate.html', context)

@user_passes_test(lambda u: u.is_superuser)
def doctor_delete(request, pk):
    doctor = Doctor.objects.get(id=pk)
    if request.method == 'POST':
        doctor.delete()
        sweetify.toast(request, 'Doctor deleted successfully', icon='success')
        return HttpResponseRedirect(reverse('doctors'))
    context = {
        'title': 'Doctor delete',
        'doctor': doctor
    }
    return render(request, 'main/doctordelete.html', context)

@user_passes_test(lambda u: u.is_superuser)
def staffs(request):
    form = StaffForm()
    if request.method == 'POST':
        form = StaffForm(request.POST)
        if form.is_valid():
            form.save()
            sweetify.toast(request, 'Staff added successfully', icon='success')
            return HttpResponseRedirect(reverse('staffs'))
    context = {
        'title': 'Staffs',
        'staffs': Staff.objects.all(),
        'form': form
    }
    return render(request, 'main/staffs.html', context)


@user_passes_test(lambda u: u.is_superuser)
def staff_update(request, pk):
    staff = Staff.objects.get(id=pk)
    form = StaffForm(instance=staff)
    if request.method == 'POST':
        form = StaffForm(request.POST, instance=staff)
        if form.is_valid():
            form.save()
            sweetify.toast(request, 'Staff updated successfully', icon='success')
            return HttpResponseRedirect(reverse('staffs'))
    context = {
        'title': 'Staff Update',
        'form': form
    }
    return render(request, 'main/staffupdate.html', context)

@user_passes_test(lambda u: u.is_superuser)
def staff_delete(request, pk):
    staff = Staff.objects.get(id=pk)
    if request.method == 'POST':
        staff.delete()
        sweetify.toast(request, 'Staff deleted successfully', icon='success')
        return HttpResponseRedirect(reverse('staffs'))
    context = {
        'title': 'Staff delete',
        'staff': staff
    }
    return render(request, 'main/staffdelete.html', context)

@login_required(login_url='login')
@verified_or_superuser
def appointments(request):
    form = AppointmentForm()
    if request.method == 'POST':
        try:
            form = AppointmentForm(request.POST)
            if form.is_valid():
                form.save() 
                sweetify.toast(request, 'Appointment added successfully', icon='success')
                return HttpResponseRedirect(reverse('appointments'))
        except:
            print('nothing')
       
        try:
            id = request.POST['appointment_id']
            appointment = Appointment.objects.get(id=id)
            appointment.status = 'Done'
            appointment.save()
            sweetify.toast(request, 'Appointment status done', icon='success')
        except:
            print('nothing')
            
    context = {
        'title': 'Appointments',
        'form': form,
        'appointments': Appointment.objects.all()
    }
    return render(request, 'main/appointments.html', context)

@login_required(login_url='login')
@verified_or_superuser
def appointment_update(request, pk):
    appointment = Appointment.objects.get(id=pk)
    form = AppointmentUpdateForm(instance=appointment)
    if request.method == 'POST':
        form = AppointmentUpdateForm(request.POST, instance=appointment)
        if form.is_valid():
            form.save()
            sweetify.toast(request, 'Appointment updated', icon='success')
            return HttpResponseRedirect(reverse('appointments'))

    context = {
        'title': 'Appointment Update',
        'form': form,
        'appointment': appointment
    }
    return render(request, 'main/appointmentupdate.html', context)


@login_required(login_url='login')
@verified_or_superuser
def appointment_delete(request, pk):
    appointment = Appointment.objects.get(id=pk)
    if request.method == 'POST':
        appointment.delete()
        sweetify.toast(request, 'Appointment deleted successfully', icon='success')
        return HttpResponseRedirect(reverse('appointments'))
    context = {
        'title': 'Appointment delete',
        'appointment': appointment
    }
    return render(request, 'main/appointmentdelete.html', context)
