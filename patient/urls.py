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

app_name = 'patient'
urlpatterns = [
    path('usermain<int:p_id>/', views.usermain, name='usermain'),
    path('updateProfile<int:p_id>/', views.updateProfile, name='updateProfile'),
    path('searchHospital<int:p_id>/', views.searchHospital, name='searchHospital'),
    path('reserveHospital/', views.reserveHospital, name='reserveHospital'),
    path('reserving/', views.reserving, name='reserving'),
    path('favorite<int:p_id>/', views.favorite, name='favorite'),
    path('deleteFavorite/', views.deleteFavorite, name='deleteFavorite'),
    path('profile<int:p_id>/', views.profile, name='profile'),
    path('reserveList<int:p_id>/', views.reserveList, name='reserveList'),
    path('selectPrescribe<int:p_id>/', views.selectPrescribe, name='selectPrescribe'),
    path('recently<int:p_id>/', views.recently, name='recently'),
    path('seePrescribe<int:p_id>/', views.seePrescribe, name='seePrescribe'),
    path('storefilter<int:p_id>/', views.storefilter, name='storefilter'),
    path('storeResult<int:p_id>/', views.storeResult, name='storeResult'),
    path('reserveStore<int:p_id>/', views.reserveStore, name='reserveStore'),
    path('reservingStore<int:p_id>/', views.reservingStore, name='reservingStore'),
    path('reserveListStore<int:p_id>/', views.reserveListStore, name='reserveListStore'),
]
