from django.shortcuts import render
from django.views import View

from lottery.models import Bet, Lottery

class BetsListView(View):
    template_name = 'lottery/bets.html'

    def get(self, request, *args, **kwargs):
        lottery = Lottery.get_current_lottery()

        context = {
            'lottery': lottery
        }
        return render(request, self.template_name, context)