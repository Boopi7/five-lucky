from django.shortcuts import render
from django.views import View
from django.http import JsonResponse


class AcceptBuyTicketNotice(View):

    def get(self, request, *args, **kwargs):
        try:
            if request.is_ajax():
                wallet_check = self.request.GET.get('walletCheck')
                terms_check = self.request.GET.get('termsCheck')

                if wallet_check != 'true':
                    raise Exception(
                        'Please accept wallet condition.')
                if terms_check != 'true':
                    raise Exception(
                        'Please accept terms and condition.')

                return JsonResponse(data = {'data': 'yey', 'status': 200})
            raise Exception('Unable to process request.')

        except Exception as e:
            return JsonResponse(data = {'error': str(e), 'status': 500})


class BuyTicketView(View):
    template_name = 'lottery/buy_ticket.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {})