from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("polls/", include("polls.urls")),  # make sure 'polls' app is included
    path("admin/", admin.site.urls),
]
