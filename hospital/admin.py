from django.contrib import admin
from .models import Hospital, Reservation, Prescription
# Register your models here.
admin.site.register(Hospital)
admin.site.register(Reservation)
admin.site.register(Prescription)