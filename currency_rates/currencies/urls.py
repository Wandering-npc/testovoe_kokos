from django.urls import path
from .views import get_currency_rate

urlpatterns = [
    path('rate/', get_currency_rate, name='get_currency_rate'),
]