from django.urls import path

from lottery.views.home import HomeView
from lottery.views.tickets import BuyTicketView

app_name = 'lottery'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('buy-ticket/', BuyTicketView.as_view(), name='buy-ticket'),
]