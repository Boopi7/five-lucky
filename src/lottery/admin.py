from django.contrib import admin
from .models import (
    Lottery,
    Bet
)


# Register your models here.
admin.site.register(Lottery)
admin.site.register(Bet)