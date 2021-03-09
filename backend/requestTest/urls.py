from django.urls import path
from .views import request


# '' => localhost:8000/api/axios
urlpatterns = [
    path("", request, name='axios_test'),
]
