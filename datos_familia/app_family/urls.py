from django.urls import path
from app_family.views import template1


urlpatterns = [
    path('', template1),
]