from django.db import models

class Account(models.Model):
    objects = models.Manager()
    id = models.AutoField(primary_key=True)
    a_local = models.CharField(max_length=100)
    a_domain = models.CharField(max_length=100)
    a_password = models.CharField(max_length=100)

    a_patient = models.ForeignKey("patient.Patient", null=True, on_delete=models.SET_NULL)
    a_hospital = models.ForeignKey("hospital.Hospital", null=True, on_delete=models.SET_NULL)
    a_store = models.ForeignKey("store.Store", null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.a_local