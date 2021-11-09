from django.shortcuts import render
from django.views import View


class HomeView(View):
    template_name = 'bets/homepage.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {})


class BuyTicketView(View):
    template_name = 'bets/buyticket.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {})