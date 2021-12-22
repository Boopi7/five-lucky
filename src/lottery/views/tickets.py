from django.shortcuts import render
from django.views import View
from django.http import JsonResponse


class AcceptBuyTicketNotice(View):

    def get(self, request, *args, **kwargs):
        try:
            if request.is_ajax():
                wallet_check = self.request.GET.get('walletCheck')
                terms_check = self.request.GET.get('termsCheck')

                if not (wallet_check == 'true' and terms_check == 'true'):
                    raise Exception('You must accept all terms and conditions.')

                return JsonResponse(data = {'data': 'yey', 'status_code': 200})

            raise Exception('Unable to process request.')

        except Exception as e:
            return JsonResponse(data = {'message': str(e), 'status_code': 500})


class BuyTicketView(View):
    template_name = 'lottery/buy_ticket.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {})