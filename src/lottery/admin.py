from django.contrib import admin
from .models import (
    LuckyFive,
    Lottery,
    Bet
)


# Register your models here.
admin.site.register(LuckyFive)
admin.site.register(Lottery)
admin.site.register(Bet)