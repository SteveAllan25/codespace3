# event_registration/urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('events.urls')),  #  Include our app's URLs
    path('accounts/', include('django.contrib.auth.urls')),
]
