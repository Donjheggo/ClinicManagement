from django.db import models
from account.models import *
import datetime
from django.utils import timezone



class Patient(models.Model):
    last_name = models.CharField(max_length=50, null=True)
    first_name = models.CharField(max_length=50, null=True)
    birthday = models.DateField(null=True)
    gender = models.CharField(choices=(('Male','Male'), ('Female', 'Female')), max_length=10)
    address = models.CharField(max_length=250)
    phone_number = models.DecimalField(max_digits=13, decimal_places=0)
    status = models.CharField(choices=(('Approved','Approved'), ('Pending', 'Pending')), max_length=10, null=True, blank=True, default='Pending')
    prescription = models.TextField(null=True, blank=True)


    def __str__(self):
        return f'{self.last_name}, {self.first_name}'


class Doctor(models.Model):
    last_name = models.CharField(max_length=50, null=True)
    first_name = models.CharField(max_length=50, null=True)
    birthday = models.DateField(null=True)
    gender = models.CharField(choices=(('Male','Male'), ('Female', 'Female')), max_length=10)
    address = models.CharField(max_length=250)
    phone_number = models.DecimalField(max_digits=13, decimal_places=0)
    specialization = models.CharField(max_length=50)
    available_day = models.CharField(max_length=50, null=True)
    available_time = models.CharField(max_length=50, null=True)

    def __str__(self):
        return f'{self.last_name}, {self.first_name}'


class Staff(models.Model):
    last_name = models.CharField(max_length=50, null=True)
    first_name = models.CharField(max_length=50, null=True)
    birthday = models.DateField(null=True)
    gender = models.CharField(choices=(('Male','Male'), ('Female', 'Female')), max_length=10)
    address = models.CharField(max_length=250)
    phone_number = models.DecimalField(max_digits=13, decimal_places=0)


    def __str__(self):
        return f'{self.last_name}, {self.first_name}'


class Appointment(models.Model):
    name = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    schedule = models.DateTimeField()
    status = models.CharField(choices=(('Done','Done'), ('Pending', 'Pending')), max_length=10, default='Pending')

    def __str__(self):
        return f'{self.name}'


