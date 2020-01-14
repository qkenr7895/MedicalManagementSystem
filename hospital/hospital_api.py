import os
import django
import json
import requests
import sys
from .models import Hospital

def hosp_list(name='defaultName121443', radius=5000, lat=37.5585146, lng=127.0331892):
    url = "http://apis.data.go.kr/B551182/hospInfoService/getHospBasisList"
    default_key = "DRUCroATfR0Xj6acPKvi1QUKy9uHDYi1CdG912PAS1H0pBRe+w7K5p4Igrq01C1pVj6PeDGjTE/EUqSXhdTwiw=="

    if name == 'defaultName121443':
      params = {
        'ServiceKey': default_key,
          'pageNo': 1,
          'numOfRows': 9999,
          'radius':radius,
          'xPos':lng,
          'yPos':lat,
          '_type': 'json'
      }
    else :
      params = {
        'ServiceKey': default_key,
          'pageNo': 1,
          'numOfRows': 9999,
          'yadmNm':name,
          'radius':radius,
          'xPos':lng,
          'yPos':lat,
          '_type': 'json'
      }
    loop = 1
    while loop == 1:
      r = requests.get(url, params=params)    
      if r.status_code == 200:
        loop = 0
      else :
        print('error')   
        print('error')
        print('error')
        print('error')
        print('error')
        print('error')
        print('error')
        print('error')
        print('error')
        print('error')

    
    return r.json()

def medical_course(ykiho):
    url = "http://apis.data.go.kr/B551182/medicInsttDetailInfoService/getMdlrtSbjectInfoList"
    default_key = "DRUCroATfR0Xj6acPKvi1QUKy9uHDYi1CdG912PAS1H0pBRe+w7K5p4Igrq01C1pVj6PeDGjTE/EUqSXhdTwiw=="
    params = {
      'ServiceKey': default_key,
        'pageNo': 1,
        'numOfRows': 9999,
        'ykiho':ykiho,
        '_type': 'json'
    }
    loop = 1
    while loop == 1:
      r = requests.get(url, params=params)    
      if r.status_code == 200:
        loop = 0
      else :
        print('error')   
        print('error')
        print('error')
        print('error')
        print('error')
        print('error')
        print('error')
        print('error')
        print('error')
        print('error') 

    return r.json()


def pharm_list(name='defaultName121443', radius=5000, lat=37.5585146, lng=127.0331892):    
    url = "http://apis.data.go.kr/B551182/pharmacyInfoService/getParmacyBasisList"
    default_key = "DRUCroATfR0Xj6acPKvi1QUKy9uHDYi1CdG912PAS1H0pBRe+w7K5p4Igrq01C1pVj6PeDGjTE/EUqSXhdTwiw=="

    if name == 'defaultName121443':
      params = {
        'ServiceKey': default_key,
          'pageNo': 1,
          'numOfRows': 9999,
          'radius':radius,
          'xPos':lng,
          'yPos':lat,
          '_type': 'json'
      }
    else :
      params = {
        'ServiceKey': default_key,
          'pageNo': 1,
          'numOfRows': 9999,
          'yadmNm':name,
          'radius':radius,
          'xPos':lng,
          'yPos':lat,
          '_type': 'json'
      }
    loop = 1
    while loop == 1:
      r = requests.get(url, params=params)    
      if r.status_code == 200:
        loop = 0
      else :
        print('error')   
        print('error')
        print('error')
        print('error')
        print('error')
        print('error')
        print('error')
        print('error')
        print('error')
        print('error')
        
    return r.json()