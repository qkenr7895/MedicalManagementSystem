from django.shortcuts import render
from .models import Store, ReservationStore
from hospital.models import Prescription
from account.models import Account
from django.core.exceptions import ObjectDoesNotExist
from patient.models import Patient
import datetime
import sys
# Create your views here.

def storemain(request, s_id):
    s = Store.objects.get(id=s_id)
    return render(request, 'storemain.html', {'s':s})

def storeprofile(request, s_id):
    s = Store.objects.get(id=s_id)
    return render(request, 'storeprofile.html', {'s':s})

def storeReservationList(request, s_id):
    s = Store.objects.get(id=s_id)
    if request.method == 'POST':
        r_id = request.POST['r_id']
        r = ReservationStore.objects.get(id=r_id)
        pre = r.r_prescription
        return render(request, 'seePrescriptionStore.html', {'s':s, 'ps':pre, 'r':r})

    rs = ReservationStore.objects.filter(r_store=s, r_type='확인중')
    return render(request, 'storeReservationList.html', {'s':s, 'rs':rs})

def deleteReserve(request, s_id):
    s = Store.objects.get(id=s_id)
    r_id = request.POST['r_id']
    r = ReservationStore.objects.get(id=r_id)
    r.delete()

    return render(request, 'storemain.html', {'s':s})

def storePrescribe(request, s_id):
    r_id = request.POST['r_id']
    p_id = request.POST['p_id']
    s = Store.objects.get(id=s_id)
    r = ReservationStore.objects.get(id=r_id)
    p = Prescription.objects.get(id=p_id)
    return render(request, 'storePrescribe.html', {'s':s, 'r':r, 'p':p})

def storePrescribeComplete(request, s_id):
    p_else = request.POST['ae']
    r_id = request.POST['r_id']
    p_id = request.POST['p_id']
    print('=============================', file=sys.stderr)
    print(p_id, file=sys.stderr)
    print('=============================', file=sys.stderr)
    s = Store.objects.get(id=s_id)
    r = ReservationStore.objects.get(id=r_id)
    p = Prescription.objects.get(id=p_id)

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

    p.p_complete_date = str(yr)+'-'+str(mon)+'-'+str(day)
    p.p_complete_time = str(hr)+':'+str(m)
    p.p_else = p_else
    p.p_store = s
    p.save()
    r.r_type = '처방완료'
    r.save()

    return render(request, 'storemain.html', {'s':s})

def storefiltering(request, s_id):
    s = Store.objects.get(id=s_id)

    if request.method == 'POST':
        p_date = request.POST['date']
        p_name = request.POST['name']
        p_id = request.POST['number']

        ps = Prescription.objects.filter(p_store=s)
        if p_date != 'none':
            ps = ps.filter(p_date=p_date)
        if p_name != 'none':
            ps = ps.filter(p_name__contains=p_name)
        if p_id != 'none':
            ps = ps.filter(id=p_id)
        
        return render(request, 'seeStoreFiltering.html', {'s':s, 'ps':ps})

    return render(request, 'storefiltering.html', {'s':s})

def prescribeAvailable(request, s_id):
    s = Store.objects.get(id=s_id)
    r_id = request.POST['r_id']

    r = ReservationStore.objects.get(id=r_id)
    r.r_type = '처방가능'
    r.save()

    return render(request, 'storemain.html', {'s':s})


def prescribeNotAvailable(request, s_id):
    s = Store.objects.get(id=s_id)
    r_id = request.POST['r_id']

    r = ReservationStore.objects.get(id=r_id)

    r.r_type = '처방불가능'
    r.save()

    return render(request, 'storemain.html', {'s':s})

def storePrescribePatient(request, s_id):
    s = Store.objects.get(id=s_id)

    if request.method == 'POST':
        r_id = request.POST['r_id']
        p_id = request.POST['p_id']
        print('---------------------', file=sys.stderr)
        print(p_id, file=sys.stderr)
        print('---------------------', file=sys.stderr)

        r = ReservationStore.objects.get(id=r_id)
        p = Prescription.objects.get(id=p_id)

        return render(request, 'storePrescribe.html', {'s':s, 'r':r, 'p':p})

    
    rs = ReservationStore.objects.filter(r_store=s, r_type='처방가능')

    return render(request, 'reservationListPres.html', {'s':s, 'rs':rs})