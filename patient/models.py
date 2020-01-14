from django.db import models

# Create your models here.
class Patient(models.Model):
    objects = models.Manager()
    id = models.AutoField(primary_key=True)
    p_name = models.CharField(max_length=100)
    p_phone = models.CharField(max_length=100)
    p_latitude = models.CharField(max_length=100)
    p_longitude = models.CharField(max_length=100)

    p_account = models.ForeignKey("account.Account", null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.p_name


class Favorite(models.Model):
    objects = models.Manager()
    id = models.AutoField(primary_key=True)

    f_patient = models.ForeignKey("patient.Patient", null=True, on_delete=models.SET_NULL)
    f_hospital = models.ForeignKey("hospital.Hospital", null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return str(self.id)