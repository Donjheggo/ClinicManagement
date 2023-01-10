from django import forms
from .models import *





class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['name', 'doctor', 'schedule']
        exclude = ['status',]
        widgets = {
            'name': forms.Select(attrs={'class': 'form-control'}),
            'doctor': forms.Select(attrs={'class': 'form-control'}),
            'schedule': forms.TextInput(attrs={'type': 'date', 'class': 'form-control'}),
        }


class AppointmentUpdateForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields ='__all__'
        widgets = {
            'name': forms.Select(attrs={'class': 'form-control'}),
            'doctor': forms.Select(attrs={'class': 'form-control'}),
            'schedule': forms.TextInput(attrs={'type': 'datetime-local', 'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
        }


class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ['last_name','first_name',  'birthday', 'gender', 'address', 'phone_number']
        exclude = ['prescription', 'status']
        widgets = {
            'last_name': forms.TextInput(attrs={'type': 'text', 'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'type': 'text', 'class': 'form-control'}),
            'birthday': forms.TextInput(attrs={'type': 'date', 'class': 'form-control'}),
            'gender': forms.Select(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'type': 'text', 'class': 'form-control'}),
            'phone_number': forms.TextInput(attrs={'type': 'number', 'class': 'form-control'}),

        }


class StaffForm(forms.ModelForm):
    class Meta:
        model = Staff
        fields ='__all__'
        widgets = {
            'last_name': forms.TextInput(attrs={'type': 'text', 'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'type': 'text', 'class': 'form-control'}),
            'birthday': forms.TextInput(attrs={'type': 'date', 'class': 'form-control'}),
            'gender': forms.Select(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'type': 'text', 'class': 'form-control'}),
            'phone_number': forms.TextInput(attrs={'type': 'number', 'class': 'form-control'}),

        }



class PatientForm_Doctor(forms.ModelForm):
    class Meta:
        model = Patient
        fields = '__all__'
        widgets = {
            'last_name': forms.TextInput(attrs={'type': 'text', 'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'type': 'text', 'class': 'form-control'}),
            'birthday': forms.TextInput(attrs={'type': 'date', 'class': 'form-control'}),
            'gender': forms.Select(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'type': 'text', 'class': 'form-control'}),
            'phone_number': forms.TextInput(attrs={'type': 'number', 'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
            'prescription': forms.Textarea(attrs={'class': 'form-control'}),
        }




class DoctorForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = '__all__'
        widgets = {
            'last_name': forms.TextInput(attrs={'type': 'text', 'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'type': 'text', 'class': 'form-control'}),
            'birthday': forms.TextInput(attrs={'type': 'date', 'class': 'form-control'}),
            'gender': forms.Select(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'type': 'text', 'class': 'form-control'}),
            'phone_number': forms.TextInput(attrs={'type': 'number', 'class': 'form-control'}),
            'specialization': forms.TextInput(attrs={'type': 'text', 'class': 'form-control'}),
            'available_day': forms.TextInput(attrs={'type': 'text', 'class': 'form-control', 'placeholder': 'Ex. Monday, Wednesday, Friday'}),
            'available_time': forms.TextInput(attrs={'type': 'text', 'class': 'form-control', 'placeholder': 'Ex. 8AM to 11AM'}),
        }
