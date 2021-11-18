import subprocess

from datetime import datetime, timezone
from django.conf import settings

from lottery.models import Lottery
from lottery.cardano.operations import (
    generate_minting_policy)


# Every Monday 00:00 UTC
def new_lottery():
    # Create directory for the new policy
    dir_name = datetime.now(
        timezone.utc).strftime('%m_%d_%y')
    policy_path = settings.POLICY_DIR + dir_name
    subprocess.run(['mkdir', '-p', policy_path])

    # Generate policy script for minting
    policyID = generate_minting_policy(policy_path)

    # Create a lottery object every week
    # Lottery.objects.create()
    pass


# Every Sunday 09:00 UTC
def draw_lottery():
    pass
