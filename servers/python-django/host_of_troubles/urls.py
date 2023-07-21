# host_header_app/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.show_host_header),
]
