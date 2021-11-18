import subprocess

from datetime import (
    datetime, timezone, timedelta)
from django.conf import settings

from lottery.models import Lottery
from lottery.cardano.operations import (
    generate_minting_policy)


# Every Monday 00:00 UTC
def new_lottery():
    # Create directory for the new policy
    today = datetime.now(timezone.utc)
    policy_path = settings.POLICY_DIR + \
        today.strftime('%m_%d_%y')
    subprocess.run(['mkdir', '-p', policy_path])

    # Generate minting policy for the
    # ticket nfts of this lottery
    policyID = generate_minting_policy(policy_path)

    # Get lottery draw date
    offset = 6 - today.weekday()
    lottery_day = today + timedelta(days=offset)
    draw_date = datetime(
        lottery_day.year, lottery_day.month,
        lottery_day.day,
        hour=9, minute=0,
        second=0, microsecond=0,
        tzinfo=timezone.utc
    )

    # Create lottery object
    lottery = Lottery.objects.create(
        policy_id=policyID,
        draw_date=draw_date)


# Every Sunday 09:00 UTC
def draw_lottery():
    pass
