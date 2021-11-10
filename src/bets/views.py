from datetime import datetime, timezone, timedelta

from django.shortcuts import render
from django.views import View


class HomeView(View):
    template_name = 'bets/homepage.html'

    def get(self, request, *args, **kwargs):
        # Get today in UTC
        # now_utc = datetime.now(timezone.utc)
        now_utc = datetime(2021, 11, 29, 9, 0, 0, 0, timezone.utc)
        print('Current date: ', now_utc)

        # Check if today is lottery day
        # Sunday 09:00 UTC - Monday 08:59 UTC
        weekday = now_utc.weekday()
        hour = now_utc.hour
        is_lottery = False

        if weekday == 6 or weekday == 0: #0-6, monday-sunday
            if weekday == 6 and hour >= 9:
                is_lottery = True
            elif weekday == 0 and hour < 9:
                is_lottery = True

        if is_lottery:
            # if lottery day, query result
            print("IT IS LOTTERY DAY!")
            pass

        else:
            # else get next lottery date in UTC (Sunday 09:00 UTC)
            offset = 6 - weekday
            next_lottery = now_utc + timedelta(days=offset)
            next_lottery = datetime(
                next_lottery.year, next_lottery.month, next_lottery.day,
                hour=9, minute=0,
                second=0, microsecond=0,
                tzinfo=timezone.utc
            )
            print('Next lottery is: ', next_lottery)

            # return date and create countdown timer in the frontend

        return render(request, self.template_name, {})


class BuyTicketView(View):
    template_name = 'bets/buyticket.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {})