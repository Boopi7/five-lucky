from datetime import datetime, timezone
from django.db import models
from django.contrib.postgres.fields import (
    ArrayField)


class Lottery(models.Model):
    # Determins if the particular lottery is active or not
    # True means that it is the current ongoing lottery
    # There should be only one active lottery object
    is_active = models.BooleanField(default=True)

    # The lottery draw date (Sunday 09:00 UTC)
    draw_date = models.DateTimeField()

    # The policy ID that will be used to mint 
    # the tickets in this lottery
    policy_id = models.CharField(max_length=250)

    # The random.org api response
    api_response = models.JSONField(
        null=True,
        blank=True)

    date_created = models.DateTimeField(
        auto_now_add=True)

    # Determines the sequence of the lottery object
    seq = models.PositiveIntegerField(
        null=True,
        blank=True,
        unique=True)

    def __str__(self):
        seq = 'Lottery ' + str(self.seq)
        formatted_date = self.draw_date.strftime(
            '%B %d, %Y %H:%M %Z')
        return seq + ' - ' + formatted_date

    @property
    def lucky_five(self):
        if self.api_response:
            return self.api_response.get(
                'result').get('random').get(
                'data')[0]
        return None

    @property
    def bets(self):
        return self.bet_set.all()

    @property
    def active_bets(self):
        return self.bet_set.filter(
            is_active=True,
            is_paid=True)

    @property
    def winners(self):
        return self.lotterywinner_set.all()

    def get_current_lottery():
        now = datetime.now(timezone.utc)
        current = Lottery.objects.filter(
            is_active=True,
            draw_date__gte=now).last()
        return current


class Bet(models.Model):
  	# The bettor's lucky-five number
    lucky_five = ArrayField(
        models.PositiveIntegerField(),
        size=5)

    # The address where the bettor will send ADA to
    payment_address = models.CharField(max_length=250)

    # The bettor's UTXO where the ticket-nft was sent
    bettor = models.CharField(
        max_length=250,
        null=True,
        blank=True)

    # The status of the bettor's bet if the ticket nft
    # is already minted
    is_active = models.BooleanField(default=False)

    # The status of the bettor's bet after checking if
    # he/she actually sent the ADA
    is_paid = models.BooleanField(default=False)

    # The lottery this bet is tied to
    lottery = models.ForeignKey(
        Lottery,
        null=True,
        on_delete=models.SET_NULL)

    # The ticket-nft assetID
    ticket = models.CharField(
        max_length=250,
        null=True,
        blank=True)

    def __str__(self):
        return str(self.lucky_five)


class LotteryWinner(models.Model):
    lottery = models.ForeignKey(
        Lottery,
        on_delete=models.CASCADE)

    # The bet of the winner
    bet = models.ForeignKey(
        Bet,
        on_delete=models.CASCADE)

    # Determines if the winner is paid or not
    is_fulfilled = models.BooleanField(
        default=False)

    # The transaction ID of the prize payment
    tx_id = models.CharField(
        max_length=250,
        null=True,
        blank=True)

    def __str__(self):
        return str(self.bet)