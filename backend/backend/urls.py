from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/axios/', include("requestTest.urls")),
]

# /api/axios/
