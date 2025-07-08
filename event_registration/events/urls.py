# events/urls.py

from django.urls import path
from . import views
from .views import signup


urlpatterns = [
    path('', views.event_list, name='event_list'),
    path('event/<int:pk>/', views.event_detail, name='event_detail'),
    path('event/<int:pk>/register/', views.register_event, name='register_event'),
    path('signup/', signup, name='signup'),

]
