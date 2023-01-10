from django.contrib import admin
from .models import *
from account.models import *



admin.site.register(Patient)
admin.site.register(Appointment)
admin.site.register(Doctor)
admin.site.register(Staff)


