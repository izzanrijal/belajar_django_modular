from django.urls import path
from . import views

urlpatterns = [
    path("beranda", views.page_beranda),
    path("status", views.page_status),
    path("", views.page_index)
]