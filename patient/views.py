from django.shortcuts import render
from .models import Patient, Favorite
from account.models import Account
from hospital.models import Hospital, Reservation, Prescription, medicalCourseDefault
from datetime import datetime
from django.http.response import HttpResponseRedirect
from django.urls.base import reverse
from django.core.exceptions import ObjectDoesNotExist
from math import radians, cos, sin, asin, sqrt
from hospital.hospital_api import hosp_list, medical_course, pharm_list
from store.models import Store, ReservationStore
import json
import time
import sys

# Create your views here.
def usermain(request, p_id):
    p = Patient.objects.get(id=p_id)
    return render(request, 'usermain.html', {'p': p})

def updateProfile(request, p_id):
    p = Patient.objects.get(id=p_id)

    if request.method == 'POST':
        new_latitude = request.POST['latitude']
        new_longitude = request.POST['longitude']
        p.p_latitude = new_latitude
        p.p_longitude = new_longitude
        p.save()

        return render(request, 'usermain.html', {'p':p})       

    return render(request, 'updateProfile.html', {'p':p})

def searchHospital(request, p_id):
    p = Patient.objects.get(id=p_id)
    p_lat = float(p.p_latitude)
    p_lon = float(p.p_longitude)
    hs_t = []
    hs = []

    if request.method == 'POST':
        name = request.POST['h_name']
        medicalCourse = request.POST['medical_course']
        htime = request.POST['time']

        if p_lat == 37.5585146 and p_lon == 127.0331892:
            hs = Hospital.objects.filter(h_name__contains=name)
            print(hs, file=sys.stderr)

        else:
            clinics = hosp_list(name=name, radius=100, lat=p_lat, lng=p_lon)

            if clinics['response']['body']['totalCount'] == 0:
                aasvv = 3
            elif clinics['response']['body']['totalCount'] == 1:
                temp = clinics['response']['body']['items']['item']
                h_key = temp['ykiho']
                h_name = temp['yadmNm']
                h_lat = temp['YPos']
                h_lng = temp['XPos']
                h_addr = temp['addr']
                h_sdr = temp['sdrCnt']
                js = json.loads(medicalCourseDefault)

                try:
                    new_h = Hospital.objects.get(h_name=h_name, h_key=h_key)
                except ObjectDoesNotExist:
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
                    else:
                        h_medicalCourse = json.dumps(js)

                    new_h = Hospital(h_key=h_key, h_name=h_name, h_latitude=h_lat, h_longitude=h_lng, h_address=h_addr, h_specialCount=h_sdr, h_medicalCourse=h_medicalCourse)
                    new_h.save()

                hs.append(new_h)

            else:
                for temp in clinics['response']['body']['items']['item']:
                    h_key = temp['ykiho']
                    h_name = temp['yadmNm']
                    h_lat = temp['YPos']
                    h_lng = temp['XPos']
                    h_addr = temp['addr']
                    h_sdr = temp['sdrCnt']
                    js = json.loads(medicalCourseDefault)

                    try:
                        new_h = Hospital.objects.get(h_name=h_name, h_key=h_key)
                    except ObjectDoesNotExist:
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
                        else:
                            h_medicalCourse = json.dumps(js)

                        new_h = Hospital(h_key=h_key, h_name=h_name, h_latitude=h_lat, h_longitude=h_lng, h_address=h_addr, h_specialCount=h_sdr, h_medicalCourse=h_medicalCourse)
                        new_h.save()

                    hs.append(new_h)

        for h in hs:
            print(h, file=sys.stderr)
            h_lat = float(h.h_latitude)
            h_lon = float(h.h_longitude)
            if (h.get_medicalCourse())[int(medicalCourse)] == True and haversine(float(p_lon), float(p_lat), h_lon, h_lat) < 1:           
                if htime == 'avail':
                    r = time.localtime()
                    r = r.tm_wday
                    
                    if r == 0:
                        h_open = h.h_open1
                        h_close = h.h_close1
                    elif r == 1:
                        h_open = h.h_open2
                        h_close = h.h_close2
                    elif r == 2:
                        h_open = h.h_open3
                        h_close = h.h_close3
                    elif r == 3:
                        h_open = h.h_open4
                        h_close = h.h_close4
                    elif r == 4:
                        h_open = h.h_open5
                        h_close = h.h_close5
                    elif r == 5:
                        h_open = h.h_open6
                        h_close = h.h_close6
                    elif r == 6:
                        h_open = h.h_open7
                        h_close = h.h_close7

                    now = now = datetime.now()
                    nowTime = now.strftime('%H:%M')
                    print(nowTime, file=sys.stderr)
                    print(h_open, file=sys.stderr)
                    if nowTime > h_open and nowTime < h_close:
                        hs_t.append(h)

                else :
                    hs_t.append(h)

        print(hs_t, file=sys.stderr)
        return render(request, 'searchResult.html', {'h':hs_t, 'p':p})

    return render(request, 'searchfilter.html', {'p':p})    

def reserveHospital(request):
    h_id = request.POST['h_id']
    p_id = request.POST['p_id']
    h = Hospital.objects.get(id=h_id)
    p = Patient.objects.get(id=p_id)

    return render(request, 'reserveHospital.html', {'h':h, 'p':p})

def reserving(request):
    h_id = request.POST['h_id']
    p_id = request.POST['p_id']
    r_date = request.POST['date']
    r_time = request.POST['time']

    h = Hospital.objects.get(id=h_id)
    p = Patient.objects.get(id=p_id)
    
    new_r = Reservation(r_date=r_date, r_time=r_time)
    new_r.save()
    new_r.r_patient = p
    new_r.r_hospital = h
    new_r.save()

    return HttpResponseRedirect(reverse('patient:usermain', args=(p_id,)))


def favorite(request, p_id):
    if request.method == 'POST':
        h_id = request.POST['h_id']
        h = Hospital.objects.get(id=h_id)        
        p = Patient.objects.get(id=p_id)
        
        try:
            f = Favorite.objects.get(f_patient=p, f_hospital=h)
        except ObjectDoesNotExist:
            f = Favorite()
            f.save()
            f.f_patient = p
            f.f_hospital = h
            f.save()

        return HttpResponseRedirect(reverse('patient:usermain', args=(p_id,)))
    else: 
        p = Patient.objects.get(id=p_id)
        fs = Favorite.objects.filter(f_patient=p)

        return render(request, 'favorite.html', {'p':p, 'f':fs})

def deleteFavorite(request):
    p_id = request.POST['p_id']
    f_id = request.POST['f_id']
    f = Favorite.objects.get(id=f_id)

    f.delete()

    return HttpResponseRedirect(reverse('patient:favorite', args=(p_id,)))

def haversine(lon1, lat1, lon2, lat2):
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])
    dlon = lon2 - lon1 
    dlat = lat2 - lat1 
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a)) 
    km = 6367 * c
    return km

def profile(reuqest, p_id):
    p = Patient.objects.get(id=p_id)

    return render(reuqest, 'profile.html', {'p':p})

def reserveList(request, p_id):
    p = Patient.objects.get(id=p_id)
    if request.method == 'POST':
        r_id = request.POST['r_id']
        r = Reservation.objects.get(id=r_id)
        r.delete()

        return HttpResponseRedirect(reverse('patient:usermain', args=(p_id,)))

    rs = Reservation.objects.filter(r_patient=p)

    return render(request, 'reserveList.html', {'p':p, 'rs':rs})

def selectPrescribe(request, p_id):
    p = Patient.objects.get(id=p_id) 
    ps = Prescription.objects.filter(p_patient=p)
    return render(request, 'selectPrescribe.html', {'p':p, 'ps':ps})

def seePrescribe(request, p_id):
    p = Patient.objects.get(id=p_id) 
    ps_id = request.POST['ps_id']
    ps = Prescription.objects.get(id=ps_id)

    return render(request, 'seePrescribe.html', {'p':p, 'ps':ps})

def recently(request, p_id):
    p = Patient.objects.get(id=p_id)

    ps = Prescription.objects.filter(p_patient=p)
    recent_ps = None
    for temp in ps:
        print(temp.p_hospital.h_name, file=sys.stderr)
        print(temp.p_date, file=sys.stderr)
        print(temp.p_time, file=sys.stderr)
        if recent_ps == None:
            print('none', file=sys.stderr)
            recent_ps = temp

        elif recent_ps.p_date <= temp.p_date:
            recent_ps = temp

        elif recent_ps.p_date == temp.p_date and recent_ps.p_time <= temp.p_time:
            recent_ps = temp

    print(recent_ps.p_hospital.h_name, file=sys.stderr)
    print(recent_ps.p_date, file=sys.stderr)
    print(recent_ps.p_time, file=sys.stderr)
    return render(request, 'recently.html', {'p':p, 'ps':recent_ps})

def storefilter(request, p_id):
    p = Patient.objects.get(id=p_id)
    return render(request, 'storefilter.html', {'p':p})

def storeResult(request, p_id):
    p = Patient.objects.get(id=p_id)
    s_name = request.POST['name']
    s_type = request.POST['type']
    p_latitude = float(p.p_latitude)
    p_longitude = float(p.p_longitude)

    resultss = []
    finalss = []

    if (p_latitude == 37.5585146 and p_longitude == 127.0331892) or (s_type=='일반상점'):
        resultss = Store.objects.filter(s_name__contains=s_name, s_type=s_type)
    
    elif s_type=='약국':
        pharms = pharm_list(name=s_name, radius=100, lat=p_latitude, lng=p_longitude)

        if pharms['response']['body']['totalCount'] == 0:
            resultss = None
        elif pharms['response']['body']['totalCount'] == 1:
            temp = pharms['response']['body']['items']['item']
            s_name = temp['yadmNm']
            s_addr = temp['addr']
            s_lat = temp['YPos']
            s_lng = temp['XPos']
            s_type = '약국'

            try :
                new_s = Store.objects.get(s_name=s_name, s_address=s_addr)
            except ObjectDoesNotExist:
                new_s = Store(s_name=s_name, s_address=s_addr, s_latitude=s_lat, s_longitude=s_lng, s_type=s_type)
                new_s.save()

            resultss.append(new_s)
        else :
            for temp in pharms['response']['body']['items']['item']:
                s_name = temp['yadmNm']
                s_addr = temp['addr']
                s_lat = temp['YPos']
                s_lng = temp['XPos']
                s_type = '약국'

                try:
                    new_s = Store.objects.get(s_name=s_name, s_address=s_addr)
                except ObjectDoesNotExist:
                    new_s = Store(s_name=s_name, s_address=s_addr, s_latitude=s_lat, s_longitude=s_lng, s_type=s_type)
                    new_s.save()

                resultss.append(new_s)

    for temp_s in resultss:
        temp_lat = float(temp_s.s_latitude)
        temp_lon = float(temp_s.s_longitude)

        if haversine(float(p_latitude), float(p_longitude), temp_lat, temp_lon) < 1:
            finalss.append(temp_s)

    return render(request, 'storeResult.html', {'ss':finalss, 'p':p})

def reserveStore(request, p_id):
    p = Patient.objects.get(id=p_id)
    s_id = request.POST['id']
    s = Store.objects.get(id=s_id)
    ps = Prescription.objects.filter(p_patient=p, p_store=None)
    print(ps, file=sys.stderr)
    return render(request, 'reserveStoreTime.html', {'p':p, 's':s, 'prescription':ps})

def reservingStore(request, p_id):
    s_id = request.POST['s_id']
    r_time = request.POST['time']
    r_date = request.POST['date']
    pre_id = request.POST['prescription']

    pre = Prescription.objects.get(id=pre_id)
    s = Store.objects.get(id=s_id)
    p = Patient.objects.get(id=p_id)

    new_r = ReservationStore(r_date=r_date, r_time=r_time, r_patient=p, r_store=s)
    new_r.r_prescription = pre
    new_r.save()

    return HttpResponseRedirect(reverse('patient:usermain', args=(p_id,)))

def reserveListStore(request, p_id):
    p = Patient.objects.get(id=p_id)

    if request.method == 'POST':
        r_id = request.POST['r_id']
        del_r = ReservationStore.objects.get(id=r_id)
        del_r.delete()

        return HttpResponseRedirect(reverse('patient:usermain', args=(p_id,)))

    rs = ReservationStore.objects.filter(r_patient=p)

    return render(request, 'reserveListStore.html', {'p':p, 'rs':rs})



