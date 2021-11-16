from django.urls import path

from .views import (
    HomeView,
    BuyTicketView
)

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('buy-ticket/', BuyTicketView.as_view(), name='buy-ticket'),
]