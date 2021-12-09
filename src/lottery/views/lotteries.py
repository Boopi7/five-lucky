from django.shortcuts import render
from django.views import View

from lottery.models import Lottery


class LotteryListView(View):
    template_name = 'lottery/lottery_list.html'

    def get(self, request, *args, **kwargs):
        lotteries = Lottery.objects.order_by('-seq')

        context = {
            'lotteries': lotteries
        }
        return render(request, self.template_name, context)


class LotteryDetailView(View):
    template_name = 'lottery/results.html'

    def get(self, request, *args, **kwargs):
        lotteries = Lottery.objects.filter(
            is_active=False)

        context = {
            'lotteries': lotteries
        }
        return render(request, self.template_name, context)