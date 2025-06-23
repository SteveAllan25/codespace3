from django.urls import path
from . import views

urlpatterns = [
    path('checkin/', views.check_in, name='check-in'),
    path('checkout/', views.check_out, name='check-out'),
]
