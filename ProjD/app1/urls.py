from django.urls import path
from . import views

urlpatterns = [
    path('',views.app1_hello,name="app1_hello"),
    
]
