from django.shortcuts import render
from django.views import View
from django.views.generic import DetailView

from lottery.models import Lottery


class LotteryListView(View):
    template_name = 'lottery/lottery_list.html'

    def get(self, request, *args, **kwargs):
        lotteries = Lottery.objects.order_by('-seq')

        context = {
            'lotteries': lotteries
        }
        return render(request, self.template_name, context)


class LotteryDetailView(DetailView):
    queryset = Lottery.objects.all()