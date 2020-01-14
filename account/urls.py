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

app_name = 'account'
urlpatterns = [
    path('signin/', views.signin, name='signin'),
    path('signup/', views.signup, name='signup'),
    path('patient_signup/<int:a_id>', views.patient_signup, name='patient_signup'),    
    path('hospital_search/<int:a_id>', views.hospital_search, name='hospital_search'),
    path('hospital_signup/<int:a_id>.', views.hospital_signup, name='hospital_signup'),
    path('storeSearch/<int:a_id>.', views.storeSearch, name='storeSearch'),
    path('storeSignup/<int:a_id>.', views.storeSignup, name='storeSignup'),
    path('storeSignupDefault/<int:a_id>.', views.storeSignupDefault, name='storeSignupDefault'),
]
