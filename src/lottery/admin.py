from django.contrib import admin
from .models import (
    Lottery, Bet, LotteryWinner)


# Register your models here.
# admin.site.register(Lottery)
@admin.register(Lottery)
class LotteryAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'policy_id',
        'is_active', 'lucky_five')


@admin.register(Bet)
class BetAdmin(admin.ModelAdmin):
    list_display = ('bettor', 'lucky_five',
        'lottery', 'ticket', 'is_paid',
        'is_active')