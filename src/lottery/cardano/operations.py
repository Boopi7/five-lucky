import os, subprocess

from datetime import datetime, timezone


def generate_minting_policy(policy_path):
    policy_script_file = policy_path + '/policy.script'
    policy_id_file = policy_path + '/policyID'
    vkey_file = policy_path + '/policy.vkey'
    skey_file = policy_path + '/policy.skey'

    # Generate policy key pairs
    gen_key = ('cardano-cli address key-gen '
        '--verification-key-file {0} '
        '--signing-key-file {1}').format(
        vkey_file, skey_file).split(' ')
    subprocess.run(
        gen_key,
        capture_output=True,
        text=True)

    # Generate key hash
    gen_key_hash = ('cardano-cli address key-hash '
        '--payment-verification-key-file {}').format(
        vkey_file).split(' ')
    gen_key_hash_output = subprocess.run(
        gen_key_hash,
        capture_output=True,
        text=True)
    key_hash = gen_key_hash_output.stdout.strip()

    # Create policy script
    script = ('\n    "keyHash": "{}",'
        '\n    "type": "sig"\n').format(key_hash)
    f = open(policy_script_file, 'w')
    f.write("{" + script + "}\n")
    f.close()

    # Generate policyID
    gen_policyID = ('cardano-cli transaction policyid '
        '--script-file {0}').format(
        policy_script_file).split(' ')
    gen_policyID_output = subprocess.run(
        gen_policyID,
        capture_output=True,
        text=True)
    policyID = gen_policyID_output.stdout.strip()

    f = open(policy_id_file, 'w')
    f.write(policyID)
    f.close()

    return policyID