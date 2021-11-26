from datetime import datetime, timezone, timedelta

from django.shortcuts import render
from django.views import View
from lottery.models import Lottery


class HomeView(View):
    template_name = 'lottery/homepage.html'

    def get(self, request, *args, **kwargs):
        # Get current lottery
        lottery = Lottery.objects.last()

        context = {
            'lottery': lottery
        }

        return render(request, self.template_name, context)