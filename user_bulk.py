import os
import django
import csv
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'medical_management_system.settings')
django.setup()

from account.models import Account
from patient.models import Patient

f = open('customers.csv', 'r', encoding='utf-8')
info = []
rdr = csv.reader(f)
for row in rdr:
    name, phone, local, domain, passwd, payments, lat, lng = row
    tuple = (name, phone, local, domain, passwd, payments, lat, lng)
    info.append(tuple)
f.close()

count = 0
instancesa = []
instancesp = []
for (name, phone, local, domain, passwd, payments, lat, lng) in info:
    if name != 'name' and phone != 'phone':
        if count % 100 == 0:
            print(count)
        a = Account(a_local=local, a_domain=domain, a_password=passwd)
        p = Patient(p_name=name, p_phone=phone, p_latitude=lat, p_longitude=lng)
        a.save()
        p.save()
        a.a_patient = p
        p.p_account = a
        a.save()
        p.save()
        count += 1


