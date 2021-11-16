from django.shortcuts import render
from django.views import View


class BuyTicketView(View):
    template_name = 'lottery/buyticket.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {})