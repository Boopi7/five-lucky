from django.shortcuts import render
from django.views import View

from lottery.models import Lottery

class ResultsView(View):
    template_name = 'lottery/results.html'

    def get(self, request, *args, **kwargs):
        lotteries = Lottery.objects.filter(
            is_active=False)

        context = {
            'lotteries': lotteries
        }
        return render(request, self.template_name, context)