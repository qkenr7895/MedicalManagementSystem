import os
import django
import json
import requests
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'medical_management_system.settings')
django.setup()
from store.models import Store
from hospital.hospital_api import pharm_list

if __name__ == ("__main__"):
    count = 1
    info = []
    instances = []
    pharms = pharm_list()

    total = int(pharms['response']['body']['totalCount'])
    print(total)
    for temp in pharms['response']['body']['items']['item']:
        print(count)        
        h_name = temp['yadmNm']
        h_lat = temp['YPos']
        h_lng = temp['XPos']
        h_addr = temp['addr']
        h_type = '약국'

        tuple = (h_name, h_lat, h_lng, h_addr, h_type)
        info.append(tuple)
        count += 1
        
    for (h_name, h_lat, h_lng, h_addr, h_type) in info:
        instances.append(Store(s_name=h_name, s_latitude=h_lat, s_longitude=h_lng, s_address=h_addr, s_type=h_type))

    Store.objects.bulk_create(instances)
    print('success')

