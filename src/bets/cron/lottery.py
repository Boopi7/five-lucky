import subprocess

from django.conf import settings
from bets.models import Lottery


# Every Monday 00:00 UTC
def new_lottery():
    # Generate policy script for minting

    # Create a lottery object every week
    process = subprocess.run(
        ['which', 'cardano-cli'],
        capture_output=True,
        text=True)
    print(process)
    print(process.stdout)
    pass


# Every Sunday 09:00 UTC
def draw_lottery():
    pass
