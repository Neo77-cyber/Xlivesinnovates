from django.urls import path
from . import views



urlpatterns = [
    path('', views.home, name = 'home' ),
    path('signin/', views.signin, name = 'signin' ),
    path('farmrecords/', views.farm_records, name = 'farmrecords' ),
    path('success/', views.success, name = 'success' ),


    
]