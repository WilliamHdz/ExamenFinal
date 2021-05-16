
from django.contrib import admin
from django.urls import path
from login.views import logon, logout_view
from EF201801580.views import homepage

urlpatterns = [
    path('admin/', admin.site.urls, name="entrada"),
    path('login/',logon, name="login"),
    path('logout/',logout_view, name="logout"),
    path('',homepage, name="homepage")
]
