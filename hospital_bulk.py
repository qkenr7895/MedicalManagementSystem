import os
import django
import json
import requests
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'medical_management_system.settings')
django.setup()
from hospital.models import Hospital, medicalCourseDefault
from hospital.hospital_api import hosp_list, medical_course

if __name__ == ("__main__"):
    count = 0
    info = []
    instances = []
    clinics = hosp_list()

    total = int(clinics['response']['body']['totalCount'])
    print(total)
    for temp in clinics['response']['body']['items']['item']:
        print(count)
        h_key = temp['ykiho']
        h_name = temp['yadmNm']
        h_lat = temp['YPos']
        h_lng = temp['XPos']
        h_addr = temp['addr']
        h_sdr = temp['sdrCnt']
        js = json.loads(medicalCourseDefault)

        mc = medical_course(h_key)

        if mc['response']['body']['totalCount'] != 0:
            if mc['response']['body']['totalCount'] == 1:
                index = int(mc['response']['body']['items']['item']['dgsbjtCd'])
                js[index] = True

            else :
                for medi in mc['response']['body']['items']['item']:
                    index = int(medi['dgsbjtCd'])
                    js[index] = True

            h_medicalCourse = json.dumps(js)
            tuple = (h_key, h_name, h_lat, h_lng, h_addr, h_sdr, h_medicalCourse)
            info.append(tuple)
        count += 1
        
    for (h_key, h_name, h_lat, h_lng, h_addr, h_sdr, h_medicalCourse) in info:
        instances.append(Hospital(h_key=h_key, h_name=h_name, h_latitude=h_lat, h_longitude=h_lng, h_address=h_addr, h_specialCount=h_sdr, h_medicalCourse=h_medicalCourse))

    Hospital.objects.bulk_create(instances)
    print('success')

