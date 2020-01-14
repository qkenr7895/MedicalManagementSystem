from django.shortcuts import render
from django.http.response import HttpResponseRedirect
from django.urls.base import reverse
from .models import Account
from django.core.exceptions import ObjectDoesNotExist
from patient.models import Patient
from hospital.models import Hospital, medicalCourseDefault
from store.models import Store
from hospital.hospital_api import hosp_list, medical_course, pharm_list
import sys
import json

def signin(request):
    if request.method == 'POST':
        local = request.POST['local']
        domain = request.POST['domain']
        pw = request.POST['pw']

        try:
            ac = Account.objects.get(a_local=local, a_domain=domain, a_password=pw)
        except ObjectDoesNotExist:
            return render(request, 'signin.html', {'error':'로그인에 실패했습니다'})

        print(ac.a_patient, file=sys.stderr)
        return render(request, 'select_type.html', {'a':ac})

    return render(request, 'signin.html')

def signup(request):
    if request.method == 'POST':
        local = request.POST['local']
        domain = request.POST['domain']
        password = request.POST['pw']

        if request.POST['pw'] != request.POST['pwcheck']:
            return render(request, 'signup.html', {'error':'비밀번호가 다릅니다'})
        try:
            ac = Account.objects.get(a_local=local, a_domain=domain)
        except ObjectDoesNotExist:
            new_ac = Account(a_local=local, a_domain=domain, a_password=password)
            new_ac.save()
            return render(request, 'select_signup.html', {'a':new_ac})

        if ac.a_password == password:
            return render(request, 'select_signup.html', {'a':ac})
        else:
            return render(request, 'signup.html', {'error':'이미 존재하는 아이디입니다'})

    return render(request, 'signup.html')

def patient_signup(request, a_id):
    ac = Account.objects.get(id=a_id)
    if request.method == 'POST':
        name = request.POST['name']
        phone = request.POST['phone']
        latitude = request.POST['latitude']
        longitude = request.POST['longitude']

        new_p = Patient(p_name=name, p_phone=phone, p_latitude=latitude, p_longitude=longitude)
        new_p.save()
        ac.a_patient = new_p
        new_p.p_account = ac
        ac.save()
        new_p.save()
        return HttpResponseRedirect(reverse('patient:usermain', args=(new_p.id,)))

    return render(request, 'patient_signup.html', {'a':ac})

def hospital_signup(request, a_id):
    ac = Account.objects.get(id=a_id)
    
    key = request.POST['ykiho']
    name = request.POST['name']
    latitude = request.POST['lat']
    longitude = request.POST['lng']
    address = request.POST['addr']
    specialCount = request.POST['spc']

    try:
        h = Hospital.objects.get(h_key=key, h_name=name, h_latitude=latitude, h_longitude=longitude)
    except ObjectDoesNotExist:
        new_h = Hospital(h_key=key, h_name=name, h_latitude=latitude, h_longitude=longitude, h_address=address, h_specialCount=specialCount)

        js = json.loads(medicalCourseDefault)
        mc = medical_course(key)

        if mc['response']['body']['totalCount'] == 1:
            index = int(mc['response']['body']['items']['item']['dgsbjtCd'])
            js[index] = True
        elif mc['response']['body']['totalCount'] > 1:    
            for medi in mc['response']['body']['items']['item']:
                index = int(medi['dgsbjtCd'])
                js[index] = True

        h_medicalCourse = json.dumps(js)
        new_h.h_medicalCourse = h_medicalCourse
        new_h.save()

        ac.a_hospital = new_h
        new_h.h_account = ac
        new_h.save()
        ac.save()

        return HttpResponseRedirect(reverse('hospital:hospitalmain', args=(new_h.id,)))

    if h.h_account is None:
        h.h_account = ac
        ac.a_hospital = h
        h.save()
        ac.save()

        return HttpResponseRedirect(reverse('hospital:hospitalmain', args=(h.id,)))

    return render(request, 'hospital_search.html', {'a':ac,'error':'이미 등록된 병원입니다'})

def hospital_search(request, a_id):
    hs = []
    ac = Account.objects.get(id=a_id)
    if request.method == 'POST':
        h_name = request.POST['name']
        h_latitude = float(request.POST['latitude'])
        h_longitude = float(request.POST['longitude'])

        if h_latitude == 37.5585146 and h_longitude == 127.0331892:
            try:
                h = Hospital.objects.filter(h_name__contains=h_name)
            except ObjectDoesNotExist:
                return render(request, 'hospital_search.html', {'a':ac,'error':'검색 결과가 없습니다. 다시 입력해주세요'})
            return render(request, 'hospital_signup.html', {'hq':h, 'a':ac})
        else: 
            clinics = hosp_list(name=h_name, radius=500, lat=h_latitude, lng=h_longitude)
            if clinics['response']['body']['totalCount'] == 0:
                return render(request, 'hospital_search.html', {'a':ac,'error':'검색 결과가 없습니다. 다시 입력해주세요'})
            elif clinics['response']['body']['totalCount'] == 1:
                hs.append(clinics['response']['body']['items']['item'])
                return render(request, 'hospital_signup.html', {'hs':hs, 'a':ac})

            clinics_dict = clinics['response']['body']['items']['item']
            return render(request, 'hospital_signup.html', {'hs':clinics_dict, 'a':ac})
        
    return render(request, 'hospital_search.html', {'a':ac})

def storeSearch(request, a_id):
    ss = []
    ac = Account.objects.get(id=a_id)
    if request.method == 'POST':
        s_name = request.POST['name']
        s_latitude = float(request.POST['latitude'])
        s_longitude = float(request.POST['longitude'])

        if s_latitude == 37.5585146 and s_longitude == 127.0331892:
            try:
                s = Store.objects.filter(s_name__contains=s_name)
            except ObjectDoesNotExist:
                return render(request, 'storeSearch.html', {'a':ac,'error':'검색 결과가 없습니다. 다시 입력해주세요'})
            return render(request, 'storeSignup.html', {'sq':s, 'a':ac})
        else: 
            pharms = pharm_list(name=s_name, radius=500, lat=s_latitude, lng=s_longitude)
            if pharms['response']['body']['totalCount'] == 0:
                return render(request, 'hospital_search.html', {'a':ac,'error':'검색 결과가 없습니다. 다시 입력해주세요'})
            elif pharms['response']['body']['totalCount'] == 1:
                ss.append(pharms['response']['body']['items']['item'])
                return render(request, 'storeSignup.html', {'ss':ss, 'a':ac})

            pharms = pharms['response']['body']['items']['item']
            return render(request, 'storeSignup.html', {'ss':pharms, 'a':ac})
        
    return render(request, 'storeSearch.html', {'a':ac})

def storeSignup(request, a_id):
    ac = Account.objects.get(id=a_id)

    s_name = request.POST['name']
    s_latitude = request.POST['lat']
    s_longitude = request.POST['lng']
    s_address = request.POST['addr']
    s_type = request.POST['type']

    try:
        s = Store.objects.get(s_name=s_name, s_latitude=s_latitude, s_type=s_type, s_longitude=s_longitude)
    except ObjectDoesNotExist:
        new_s = Store(s_name=s_name, s_latitude=s_latitude, s_longitude=s_longitude, s_address=s_address, s_type=s_type)
        new_s.save()

        ac.a_store = new_s
        new_s.s_account = ac
        new_s.save()
        ac.save()

        return HttpResponseRedirect(reverse('store:storemain', args=(new_s.id,)))

    if s.s_account is None:
        s.s_account = ac
        ac.a_store = s
        s.save()
        ac.save()

        return HttpResponseRedirect(reverse('store:storemain', args=(s.id,)))

    return render(request, 'storeSearch.html', {'a':ac,'error':'이미 등록된 병원입니다'})

def storeSignupDefault(request, a_id):
    a = Account.objects.get(id=a_id)
    if request.method == 'POST':
        s_name = request.POST['name']
        s_address = request.POST['address']
        s_latitude = request.POST['latitude']
        s_longitude = request.POST['longitude']
        s_type = request.POST['type']

        new_s = Store(s_name=s_name, s_address=s_address, s_latitude=s_latitude, s_longitude=s_longitude, s_type=s_type)
        new_s.save()
        new_s.s_account = a
        a.a_store = new_s
        new_s.save()
        a.save()

        return HttpResponseRedirect(reverse('store:storemain', args=(new_s.id,)))

    return render(request, 'storeSignupDefault.html', {'a':a})

