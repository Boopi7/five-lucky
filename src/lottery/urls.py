from django.urls import path

from lottery.views.home import HomeView
from lottery.views.tickets import BuyTicketView
from lottery.views.bets import BetsListView
from lottery.views.lotteries import LotteryListView

app_name = 'lottery'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('buy-ticket/', BuyTicketView.as_view(), name='buy-ticket'),
    path('bets/', BetsListView.as_view(), name='bets'),
    path('lotteries/', LotteryListView.as_view(), name='lotteries')
]