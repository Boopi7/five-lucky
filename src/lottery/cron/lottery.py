import subprocess

from django.conf import settings
from lottery.models import Lottery
from lottery.cardano.operations import (
    generate_minting_policy)


# Every Monday 00:00 UTC
def new_lottery():
    # Generate policy script for minting
    policyID = generate_minting_policy()
    print(policyID)

    # Create a lottery object every week
    # Lottery.objects.create()
    pass


# Every Sunday 09:00 UTC
def draw_lottery():
    pass
