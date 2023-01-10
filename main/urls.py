from django.urls import path
from django.shortcuts import redirect
from . import views

urlpatterns = [
    path('dashboard', views.dashboard, name='dashboard'),

    path('profile/<str:pk>', views.profile, name='profile'),

    path('patients', views.patients, name='patients'),
    path('patient/update/<str:pk>', views.patient_update, name='patient_update'),
    path('patient/delete/<str:pk>', views.patient_delete, name='patient_delete'),

    path('doctors', views.doctors, name='doctors'),
    path('doctor/update/<str:pk>', views.doctor_update, name='doctor_update'),
    path('doctor/delete/<str:pk>', views.doctor_delete, name='doctor_delete'),

    path('doctor/schedule', views.doctor_schedule, name='doctor_schedule'),

    path('staffs', views.staffs, name='staffs'),
    path('staff/update/<str:pk>', views.staff_update, name='staff_update'),
    path('staff/delete/<str:pk>', views.staff_delete, name='staff_delete'),

    path('appointments', views.appointments, name='appointments'),
    path('appointment/update/<str:pk>', views.appointment_update, name='appointment_update'),
    path('appointment/delete/<str:pk>', views.appointment_delete, name='appointment_delete'),

]
