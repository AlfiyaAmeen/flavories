
from django.urls import path
from.import views
urlpatterns = [
   
    path('',views.index),
    path("xyz/",views.test1),
    path("login/",views.login),
    path('register/',views.register),
    path('login/loginsub/',views.loginsub),
    path('register/regsub/',views.regsub)
]