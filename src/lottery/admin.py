from django.contrib import admin
from .models import (
    Lottery,
    Bet
)


# Register your models here.
# admin.site.register(Lottery)
@admin.register(Lottery)
class LotteryAdmin(admin.ModelAdmin):
    list_display = ('draw_date', 'policy_id',
        'is_active', 'lucky_five')


@admin.register(Bet)
class BetAdmin(admin.ModelAdmin):
    list_display = ('lucky_five', 'lottery',
        'bettor', 'ticket', 'is_paid', 'is_active')