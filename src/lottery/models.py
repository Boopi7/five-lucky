from django.db import models


# The LuckyFive that will be drawn every lottery
class LuckyFive(models.Model):
    # The result winning number
    number = models.CharField(max_length=5)

    # Something that could verify that this number
    # is truly random (random.org)
    signature = models.CharField(max_length=200)

    def __str__(self):
        return self.number


class Lottery(models.Model):
    # Determins if the particular lottery is active or not
    # True means that it is the current ongoing lottery
    # There should be only one active lottery object
    is_active = models.BooleanField(default=True)

    # Determines the order of the lottery
    # Starts with 1
    number = models.PositiveIntegerField(unique=True)

    # The lottery draw date (Sunday 09:00 UTC)
    draw_date = models.DateTimeField()

    # The policy ID that will be used to mint 
    # the tickets in this lottery
    policy_id = models.CharField(max_length=250)

    # The lucky-five lottery result
    lucky_five = models.OneToOneField(
        LuckyFive,
        null=True,
        blank=True,
        on_delete=models.SET_NULL)

    def __str__(self):
        return self.date

    @property
    def current(self):
        now = datetime.now(timezone.utc)
        current = Lottery.objects.filter(
            is_active=True,
            date__gte=now).first()
        return current


class Bet(models.Model):
  	# The bettor's lucky-five number
    lucky_five = models.CharField(max_length=5)

    # The address where the bettor will send ADA to
    payment_address = models.CharField(max_length=250)

    # The bettor's UTXO where the ticket-nft was sent
    bettor = models.CharField(
        max_length=250,
        null=True,
        blank=True)

    # The status of the bettor's bet after checking if
    # he/she actually sent the ADA
    is_active = models.BooleanField(default=False)

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
        return self.tx_hash