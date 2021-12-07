from django.shortcuts import render
from django.views import View

from lottery.models import Bet, Lottery

class BetsListView(View):
    template_name = 'lottery/bets.html'

    def get(self, request, *args, **kwargs):
        # Get current lottery
        lottery = Lottery.get_current_lottery()

        context = {
            'lottery': lottery,
            'bets': lottery.active_bets
        }

        return render(request, self.template_name, context)