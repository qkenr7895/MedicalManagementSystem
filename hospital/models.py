from django.db import models
import json

medicalCourseDefault = '[false, false, false, false, false, false, false, false, false, false, \
                        false, false, false, false, false, false, false, false, false, false, \
                        false, false, false, false, false, false, false, false, false, false, \
                        false, false, false, false, false, false, false, false, false, false, \
                        false, false, false, false, false, false, false, false, false, false, \
                        false, false, false, false, false, false, false, false, false, false, \
                        false, false, false, false, false, false, false, false, false, false, \
                        false, false, false, false, false, false, false, false, false, false, \
                        false, false, false, false, false, false, false, false, false, false, false]'

# Create your models here.
class Hospital(models.Model):
    objects = models.Manager()
    id = models.AutoField(primary_key=True)
    h_key = models.CharField(max_length=200)

    h_name = models.CharField(max_length=200)
    h_latitude = models.CharField(max_length=50)
    h_longitude = models.CharField(max_length=50)
    h_address = models.CharField(max_length=550)
    h_specialCount = models.CharField(max_length=10, default='0')

    h_open1 = models.CharField(max_length=10, default='09:00')
    h_close1 = models.CharField(max_length=10, default='17:00')

    h_open2 = models.CharField(max_length=10, default='09:00')
    h_close2 = models.CharField(max_length=10, default='17:00')

    h_open3 = models.CharField(max_length=10, default='09:00')
    h_close3 = models.CharField(max_length=10, default='17:00')

    h_open4 = models.CharField(max_length=10, default='09:00')
    h_close4 = models.CharField(max_length=10, default='17:00')

    h_open5 = models.CharField(max_length=10, default='09:00')
    h_close5 = models.CharField(max_length=10, default='17:00')

    h_open6 = models.CharField(max_length=10, default='09:00')
    h_close6 = models.CharField(max_length=10, default='17:00')

    h_open7 = models.CharField(max_length=10, default='09:00')
    h_close7 = models.CharField(max_length=10, default='17:00')        

    h_medicalCourse = models.CharField(max_length=1000, default=medicalCourseDefault)

    h_account = models.ForeignKey("account.Account", null=True, on_delete=models.SET_NULL)

    def set_medicalCourse(self, x):
        self.h_medicalCourse = json.dumps(x)

    def get_medicalCourse(self):
        return json.loads(self.h_medicalCourse)

    def __str__(self):
        return self.h_name

class Reservation(models.Model):
    objects = models.Manager()
    id = models.AutoField(primary_key=True)
    r_date = models.CharField(max_length=500)
    r_time = models.CharField(max_length=500, default=0)

    r_patient = models.ForeignKey("patient.Patient", null=True, on_delete=models.SET_NULL)
    r_hospital = models.ForeignKey("hospital.Hospital", null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.r_date

class Prescription(models.Model):
    objects = models.Manager()
    id = models.AutoField(primary_key=True)

    p_name = models.CharField(max_length=500, default='none')
    p_phone = models.CharField(max_length=500, default='none')

    p_date = models.CharField(max_length=500)
    p_time = models.CharField(max_length=500, default=0)
    p_else = models.CharField(max_length=5000, default='none')

    p_medicine1 = models.CharField(max_length=100, default='none')
    p_dosage1 = models.CharField(max_length=100, default='none')
    p_dosageCount1 = models.CharField(max_length=100, default='none')
    p_totalDosage1 = models.CharField(max_length=100, default='none')

    p_medicine2 = models.CharField(max_length=100, default='none')
    p_dosage2 = models.CharField(max_length=100, default='none')
    p_dosageCount2 = models.CharField(max_length=100, default='none')
    p_totalDosage2 = models.CharField(max_length=100, default='none')

    p_medicine3 = models.CharField(max_length=100, default='none')
    p_dosage3 = models.CharField(max_length=100, default='none')
    p_dosageCount3 = models.CharField(max_length=100, default='none')
    p_totalDosage3 = models.CharField(max_length=100, default='none')

    p_medicine4 = models.CharField(max_length=100, default='none')
    p_dosage4 = models.CharField(max_length=100, default='none')
    p_dosageCount4 = models.CharField(max_length=100, default='none')
    p_totalDosage4 = models.CharField(max_length=100, default='none')

    p_complete_date = models.CharField(max_length=500, default='none')
    p_complete_time = models.CharField(max_length=500, default='none')

    p_patient = models.ForeignKey("patient.Patient", null=True, on_delete=models.SET_NULL)
    p_hospital = models.ForeignKey("hospital.Hospital", null=True, on_delete=models.SET_NULL)
    p_store = models.ForeignKey("store.Store", null=True, on_delete=models.SET_NULL)
    #p_store = models.ForeignKey("store.Store", null=True, on_delete=models.SET_NULL)
    
    def __str__(self):
        return self.p_name