from django.shortcuts import render
from .models import Hospital, Reservation, Prescription
from account.models import Account
from django.core.exceptions import ObjectDoesNotExist
from patient.models import Patient
import datetime
import sys
# Create your views here.
def hospitalmain(request, h_id):
    h = Hospital.objects.get(id=h_id)
    return render(request, 'hospitalmain.html', {'h': h})

def reservationList(request, h_id):
    h = Hospital.objects.get(id=h_id)
    rs = Reservation.objects.filter(r_hospital=h)

    if request.method == 'POST':
        r_id = request.POST['id']
        r = Reservation.objects.get(id=r_id)
        r.delete()
        return render(request, 'hospitalmain.html', {'h':h})

    return render(request, 'reservationList.html', {'rs':rs, 'h':h})

def prescribeType(request, h_id):
    h = Hospital.objects.get(id=h_id)

    if request.method == 'POST':
        p_type = str(request.POST['p_type'])
        if p_type == str('normal'):
            return render(request, 'prescribe.html', {'h':h})

        elif p_type == 'reserved':
            rs = Reservation.objects.filter(r_hospital=h)
            return render(request, 'reservationListPre.html', {'rs':rs, 'h':h})

    return render(request, 'prescribeType.html', {'h':h})

def prescribe(request, h_id):
    h = Hospital.objects.get(id=h_id)

    if request.method == 'POST':
        p_local = request.POST['local']
        p_domain = request.POST['domain']
        p_name = request.POST['name']
        p_phone = request.POST['phone']

        p11 = request.POST['11']
        p12 = request.POST['12']
        p13 = request.POST['13']
        p14 = request.POST['14']

        p21 = request.POST['21']
        p22 = request.POST['22']
        p23 = request.POST['23']
        p24 = request.POST['24']

        p31 = request.POST['31']
        p32 = request.POST['32']
        p33 = request.POST['33']
        p34 = request.POST['34']

        p41 = request.POST['41']
        p42 = request.POST['42']
        p43 = request.POST['43']
        p44 = request.POST['44']

        dt = datetime.datetime.now()       

        yr = dt.year
        mon = dt.month
        day = dt.day
        hr = dt.hour
        m = dt.minute

        if mon < 10:
            mon = '0' + str(mon)

        if day < 10:
            day = '0' + str(day)

        if hr < 10:
            hr = '0' + str(hr)

        if m < 10:
            m = '0' + str(m)

        p_date = str(yr)+'-'+str(mon)+'-'+str(day)
        p_time = str(hr)+':'+str(m)

        new_p = Prescription(p_date=p_date, p_time=p_time)
        new_p.save()

        new_p.p_medicine1 = p11
        new_p.p_dosage1 = p12 
        new_p.p_dosageCount1 = p13
        new_p.p_totalDosage1 = p14

        new_p.p_medicine2 = p21
        new_p.p_dosage2 = p22
        new_p.p_dosageCount2 = p23
        new_p.p_totalDosage2 = p24

        new_p.p_medicine3 = p31
        new_p.p_dosage3 = p32
        new_p.p_dosageCount3 = p33
        new_p.p_totalDosage3 = p34

        new_p.p_medicine4 = p41
        new_p.p_dosage4 = p42
        new_p.p_dosageCount4 = p43
        new_p.p_totalDosage4 = p44

        new_p.p_hospital = h
        new_p.save()

        try:
            ac = Account.objects.get(a_local=p_local, a_domain=p_domain)
        except ObjectDoesNotExist:
            new_p.p_name = p_name
            new_p.p_phone = p_phone
            new_p.save()
            return render(request, 'hospitalmain.html', {'h': h})

        p1 = ac.a_patient
        
        new_p.p_patient = p1
        new_p.p_name = p_name
        new_p.p_phone = p_phone

        new_p.save()
        return render(request, 'hospitalmain.html', {'h': h})

    return render(request, 'prescribe.html', {'h':h})

def reservedPrescribe(request, h_id):
    p_id = request.POST['p_id']
    r_id = request.POST['r_id']
    p = Patient.objects.get(id=p_id)
    r = Reservation.objects.get(id=r_id)    
    h = Hospital.objects.get(id=h_id)

    r.delete()

    return render(request, 'prescribe.html', {'h':h, 'p':p})

def updateHospital(request, h_id):
    h = Hospital.objects.get(id=h_id)

    if request.method == 'POST':
        o1 = request.POST['open1']
        o2 = request.POST['open2']
        o3 = request.POST['open3']
        o4 = request.POST['open4']
        o5 = request.POST['open5']
        o6 = request.POST['open6']
        o7 = request.POST['open7']

        c1 = request.POST['close1']
        c2 = request.POST['close2']
        c3 = request.POST['close3']
        c4 = request.POST['close4']
        c5 = request.POST['close5']
        c6 = request.POST['close6']
        c7 = request.POST['close7']

        h.h_open1 = str(o1)
        h.h_close1 = str(c1)

        h.h_open2 = str(o2)
        h.h_close2 = str(c2)

        h.h_open3 = str(o3)
        h.h_close3 = str(c3)

        h.h_open4 = str(o4)
        h.h_close4 = str(c4)

        h.h_open5 = str(o5)
        h.h_close5 = str(c5)

        h.h_open6 = str(o6)
        h.h_close6 = str(c6)

        h.h_open7 = str(o7)
        h.h_close7 = str(c7)

        h.save()

        return render(request, 'hospitalmain.html', {'h': h})

    return render(request, 'updateHospital.html', {'h':h})

def hospitalProfile(request, h_id):
    h = Hospital.objects.get(id=h_id)
    return render(request, 'hospitalprofile.html', {'h':h})

def filtering(request, h_id):
    h = Hospital.objects.get(id=h_id)

    if request.method == 'POST':
        p_date = request.POST['date']
        p_name = request.POST['name']
        p_id = request.POST['number']

        ps = Prescription.objects.filter(p_hospital=h)
        if p_date != 'none':
            ps = ps.filter(p_date=p_date)
        if p_name != 'none':
            ps = ps.filter(p_name__contains=p_name)
        if p_id != 'none':
            ps = ps.filter(id=p_id)
        
        return render(request, 'seeFiltering.html', {'h':h, 'ps':ps})

    return render(request, 'filtering.html', {'h':h})

def seePrescribe1(request, h_id):
    p_id = int(request.POST['p_id'])
    h = Hospital.objects.get(id=h_id)
    p = Prescription.objects.get(id=p_id)

    return render(request, 'seePrescribe1.html', {'ps':p, 'h':h})