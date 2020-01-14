from django.db import models

class Store(models.Model):
    objects = models.Manager()
    id = models.AutoField(primary_key=True)
    s_name = models.CharField(max_length=500, default=0)
    s_address = models.CharField(max_length=500, default=0)
    s_latitude = models.CharField(max_length=500, default=0)
    s_longitude = models.CharField(max_length=500, default=0)
    s_type = models.CharField(max_length=500, default=0)

    s_account = models.ForeignKey("account.Account", null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.s_name
        
class ReservationStore(models.Model):
    objects = models.Manager()
    id = models.AutoField(primary_key=True)
    r_date = models.CharField(max_length=500)
    r_time = models.CharField(max_length=500, default=0)

    r_type = models.CharField(max_length=500, default='확인중')

    r_patient = models.ForeignKey("patient.Patient", null=True, on_delete=models.SET_NULL)
    r_store = models.ForeignKey("store.Store", null=True, on_delete=models.SET_NULL)
    r_prescription = models.ForeignKey("hospital.Prescription", null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.r_date