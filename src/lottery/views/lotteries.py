from django.shortcuts import render
from django.views import View
from django.views.generic import (
    DetailView, ListView)

from lottery.models import Lottery


class LotteryListView(ListView):
    paginate_by = 9
    ordering = '-seq'
    queryset = Lottery.objects.all()


class LotteryDetailView(DetailView):
    queryset = Lottery.objects.all()