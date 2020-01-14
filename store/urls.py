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

app_name = 'store'
urlpatterns = [
    path('storemain<int:s_id>/', views.storemain, name='storemain'),
    path('storeprofile<int:s_id>/', views.storeprofile, name='storeprofile'),
    path('storeReservationList<int:s_id>/', views.storeReservationList, name='storeReservationList'),
    path('deleteReserve<int:s_id>/', views.deleteReserve, name='deleteReserve'),
    path('storePrescribe<int:s_id>/', views.storePrescribe, name='storePrescribe'),
    path('storePrescribeComplete<int:s_id>/', views.storePrescribeComplete, name='storePrescribeComplete'),
    path('storefiltering<int:s_id>/', views.storefiltering, name='storefiltering'),
    path('prescribeAvailable<int:s_id>/', views.prescribeAvailable, name='prescribeAvailable'),
    path('prescribeNotAvailable<int:s_id>/', views.prescribeNotAvailable, name='prescribeNotAvailable'),
    path('storePrescribePatient<int:s_id>/', views.storePrescribePatient, name='storePrescribePatient'),
]
