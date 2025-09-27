from django.urls import path
from . import views

urlpatterns = [
    path('', views.contacts_home, name='contacts_home'),
    path('contact/<int:pk>/', views.contact_detail, name='contact_detail'),
]
