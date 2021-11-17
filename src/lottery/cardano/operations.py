import os, subprocess

from datetime import datetime, timezone


def generate_minting_policy(path):
    gen_key_cmd = ('cardano-cli address key-gen '
        '--verification-key-file {}/policy.vkey '
        '--signing-key-file {}/policy.skey').format(
        path,path).split( )

    process = subprocess.run(gen_key_cmd,
        capture_output=True,
        text=True)

    print(process)
    
    return 'PolicyID: xxxxxxxxxxxxxxxxxxxx'