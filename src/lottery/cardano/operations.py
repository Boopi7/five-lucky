import os, subprocess

from datetime import datetime, timezone


def generate_minting_policy():
    process = subprocess.run(
        ['which', 'cardano-cli'],
        capture_output=True,
        text=True)
    
    return 'PolicyID: xxxxxxxxxxxxxxxxxxxx'