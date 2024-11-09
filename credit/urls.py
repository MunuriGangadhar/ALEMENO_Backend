from django.urls import path
from .views import register, check_eligibility

urlpatterns = [
    path('register/', register),
    path('check-eligibility/', check_eligibility),
]
