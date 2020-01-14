"""medical_management_system URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from . import views

app_name = 'hospital'
urlpatterns = [
    path('hospitalmain<int:h_id>/', views.hospitalmain, name='hospitalmain'),
    path('reservationList<int:h_id>/', views.reservationList, name='reservationList'),
    path('prescribeType<int:h_id>/', views.prescribeType, name='prescribeType'),
    path('prescribe<int:h_id>/', views.prescribe, name='prescribe'),
    path('reservedPrescribe<int:h_id>/', views.reservedPrescribe, name='reservedPrescribe'),  
    path('updateHospital<int:h_id>/', views.updateHospital, name='updateHospital'),    
    path('hospitalProfile<int:h_id>/', views.hospitalProfile, name='hospitalProfile'),    
    path('filtering<int:h_id>/', views.filtering, name='filtering'),    
    path('seePrescribe1<int:h_id>/', views.seePrescribe1, name='seePrescribe1'),  
]
