import os, subprocess

from datetime import datetime, timezone


def generate_minting_policy(policy_dir):
    policy_script = policy_dir + 'policy.script'
    vkey = policy_dir + 'policy.vkey'
    skey = policy_dir + 'policy.skey'

    # Create policy script file
    subprocess.run(['touch', policy_script],
        capture_output=True,
        text=True)

    # Generate policy key pairs
    gen_key = ('cardano-cli address key-gen '
        '--verification-key-file {0} '
        '--signing-key-file {1}').format(
        vkey, skey).split( )
    subprocess.run(gen_key,
        capture_output=True,
        text=True)

    # Generate key hash
    gen_key_hash = ('cardano-cli address key-hash '
        '--payment-verification-key-file {}').format(
        vkey).split( )
    output = subprocess.run(gen_key_hash,
        capture_output=True,
        text=True)
    key_hash = output.stdout.strip()

    print(key_hash)
    # write to policy script
    
    return 'PolicyID: xxxxxxxxxxxxxxxxxxxx'